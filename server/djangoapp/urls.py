""" Defines the URL patterns for this Django app, mapping URLs to view functions.

"""

""" Flow
    URL Routing: Defines the URL patterns for this Django app, mapping URLs to view functions.

    Flow:
        1. Incoming HTTP Request: A user's browser or application makes a request to a specific URL.
        > 2. Current File (urls.py): This file contains the `urlpatterns` list, which defines how URLs are matched.
        3. URL Resolution: Django's URL resolver compares the requested URL against these patterns.
        4. View Function Execution (in views.py): When a match is found, the corresponding view function is executed to handle the request.
"""

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path(route='register', view=views.registration, name='register'),
    path(route='login', view=views.login_user, name='login'),
    path(route='logout', view=views.logout_request, name='logout'),
    path(route='get_cars', view=views.get_cars, name='getcars'),
    path(route='get_dealers', view=views.get_dealerships, name='getdealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='get_dealer_details'),
    
    # path for dealer reviews view
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='get_dealer_details'),
    
    # path for add a review view
    path(route='add_review', view=views.add_review, name='add_review')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
