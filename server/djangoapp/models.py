""" Defines the database models for the car dealership application.

    This module contains the Django model definitions for representing car
    makes and car models. These models define the structure of the data stored
    in the application's database.

Flow:
    Data Layer:
        Defines database models (CarMake, CarModel) for the application.

    Flow:
        1. Request (in views.py):
                A user action triggers a request handled by a view function.
        2. Django ORM Interaction:
                The view uses Django's ORM (Object-Relational Mapper) to
                interact with the database.
        > 3. Current File (models.py):
                This file contains the definitions of the database tables
                (CarMake and CarModel) that the ORM uses.
        4. Database Query:
                The ORM translates the view's requests into SQL queries to the
                database.
        5. ORM Processing:
                The database returns raw data, which the ORM converts back into
                Python objects based on the model definitions in this file.
        6. Retrieve (data in views.py):  The view function then uses these
                Python objects to generate a response for the user.
"""

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Models


class CarMake(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'Suv'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2025,
        validators=[
            MaxValueValidator(now().year),
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return self.name
