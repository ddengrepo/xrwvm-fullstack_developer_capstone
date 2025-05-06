""" Contains the view functions that handle HTTP requests and return responses for this Django app.

    Input:
        HttpRequest: Each view function typically receives an HttpRequest object
            containing metadata about the incoming request (e.g., headers,
            query parameters, user information).

    Output:
        HttpResponse: Each view function must return an HttpResponse object
            (or a subclass like JsonResponse, TemplateResponse) that represents
            the server's response to the client.

"""

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate

from .models import CarMake, CarModel
from .restapis import get_request, analyze_review_sentiments, post_review

# Get an instance of a logger
logger = logging.getLogger(__name__)

# View functions
def get_cars(request):
    """ Retrieves a list of car models along with their makes and returns it as a JSON response.

        Checks if any car makes exist in the database. If not, it initiates the
        process of populating the car make and model data (using the `initiate()` function).
        Then, it fetches all car models, selecting the related car make for each model,
        and formats the data into a list of dictionaries containing the car model name
        and its corresponding car make name.

        Args:
            request (HttpRequest): The incoming HTTP request object.

        Returns:
            JsonResponse: A JSON response containing a dictionary with the key "CarModels".
                The value associated with this key is a list of dictionaries, where each
                dictionary represents a car model and its make, with the keys "CarModel"
                and "CarMake".
    """
    count = CarMake.objects.filter().count()
    print(count)
    if(count == 0):
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({"CarModel": car_model.name, "CarMake": car_model.car_make.name})
    return JsonResponse({"CarModels":cars})

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...

# Create a `registration` view to handle sign up request
# @csrf_exempt
# def registration(request):
# ...

def get_dealerships(request):
    """ Fetches and returns a list of dealerships as a JSON response, optionally filtered by state.

        This view function retrieves dealership data from an external API using the
        `get_request` function. If the 'state' parameter is provided in the request's
        GET parameters, it fetches dealerships for that specific state. Otherwise,
        it fetches all dealerships.

        Args:
            request (HttpRequest): The incoming HTTP request object. The 'state'
                parameter can be included in the request's GET parameters to filter
                dealerships by a specific state.

        Returns:
            JsonResponse: A JSON response containing:
                - "status": 200, indicating a successful request.
                - "dealers": A list of dealership objects (dictionaries) retrieved
                from the external API.
    """
    if(state == "All"):
        endpoint = '/fetchDealers'
    else:
        endpoint = '/fetchDealers/'+state
    dealerships = get_request(endpoint)
    return JsonResponse({"status":200, "dealers":dealerships})


def get_dealer_reviews(request,dealer_id):
    """ Fetches and analyzes reviews for a specific dealer, returning a JSON response.

        Retrieves reviews for the given dealer ID from an external API, analyzes
        the sentiment of each review, and includes the sentiment in the response.

        Args:
            request (HttpRequest): The incoming HTTP request object.
            dealer_id (int): The ID of the dealer for whom to retrieve reviews.

        Returns:
            JsonResponse: A JSON response containing:
                - "status": 200 for success (reviews found and analyzed),
                        400 for a bad request (invalid or missing dealer_id).
                - "review" (list, if status is 200): A list of review dictionaries. Each
                dictionary contains the original review details along with an added
                "sentiment" key indicating the analyzed sentiment.
                - "message" (str, if status is 400): An error message indicating a bad request.
    """
    if(dealer_id):
        endpoint = '/fetchReviews/dealer/'+str(dealer_id)
        reviews = get_request(endpoint)
        for review_detail in reviews:
            response = analyze_review_sentiments(review_detail['review'])
            print(response)
            review_detail['sentiment'] = response['sentiment']
        return JsonResponse({"status": 200, "review":reviews})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})


def get_dealer_details(request, dealer_id):
    """ Fetches and returns the details of a specific dealer as a JSON response.

        Retrieves dealer information based on the provided dealer ID from an
        external API.

        Args:
            request (HttpRequest): The incoming HTTP request object.
            dealer_id (int): The ID of the dealer to retrieve details for.

        Returns:
            JsonResponse: A JSON response containing:
                - "status": 200 for success (dealer details found),
                        400 for a bad request (invalid or missing dealer_id).
                - "dealer" (dict, if status is 200): A dictionary containing all
                the details of the requested dealer, as returned by the external API.
                - "message" (str, if status is 400): An error message indicating a bad request.
    """
    if(dealer_id):
        endpoint = '/fetchDealers/'+str(dealer_id)
        dealership = get_request(endpoint)
        return JsonResponse({"status": 200, "dealer":dealership})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})

        
def add_review(request):
    """ Handles the submission of a new dealership review from an authenticated user.

        This view function checks if the user is authenticated. If so, it parses the
        incoming JSON request body, calls the `post_review` function to send the
        review data to the backend API, and returns a JSON response indicating
        the success or failure of the operation. If the user is not authenticated,
        it returns an unauthorized response.

        Args:
            request (HttpRequest): The incoming HTTP request object. The request
                body is expected to contain the review data in JSON format.

        Returns:
            JsonResponse: A JSON response containing:
                - "status": 200 if the review was successfully posted to the backend.
                - "status": 401 if there was an error during the review posting process.
                The response will also include a "message" key with an error description.
                - "status": 403 if the user is not authenticated. The response will
                also include a "message" key indicating "Unauthorized".
    """
    if(request.user.is_anonymous == False):
        data = json.loads(request.body)
        try:
            response = post_review(data)
            return JsonResponse({"status": 200})
        except:
            return JsonResponse({"status": 401, "message": "Error in posting review"})
    else:
        return JsonResponse({"status": 403, "message": "Unauthorized"})

