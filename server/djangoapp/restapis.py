""" Defines functions for interacting with external REST APIs related to dealership data and sentiment analysis.

    This module provides functions that make HTTP requests (GET and POST) to backend
    services to retrieve information about dealerships, reviews, and to analyze
    the sentiment of review text. It handles the construction of URLs, sending
    requests, and processing the JSON responses. Error handling for network
    exceptions is also included.
    
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    """ Sends a GET request to the backend URL's endpoint with optional parameters
        
        Returns:
            the JSON response or None on network error. 
    """
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        return response.json()
    except:
        print("Network exception occurred")


def analyze_review_sentiments(text):
    """ Sends a GET request to the sentiment analyzer microservice for text analysis
    
        Returns: 
            the JSON response or None on error.
    """
    request_url = sentiment_analyzer_url+"analyze/"+text
    try: 
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f'Unexpected {err=}, {type(err)=}')
        print('Network exception occurred..')


def post_review(data_dict):
    """ Sends a POST request to the backend URL's "/insert_review" endpoint to add a new dealership review.

        Takes a dictionary containing the review data and transmits it as a JSON payload
        in the request body.

        Args:
            data_dict (dict): A dictionary containing the key-value pairs for all
                the required fields of a dealership review (e.g., 'dealership_id',
                'review', 'rating', 'purchase_date', 'car_make', 'car_model').

        Returns:
            dict: The JSON response from the backend after attempting to add the review.
                This might include information about the success or failure of the
                operation. Returns None if a network exception occurs.
    """
    request_url = backend_url+"/insert_review"
    try:
        response: requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
