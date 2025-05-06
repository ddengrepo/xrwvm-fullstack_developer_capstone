""" Defines the database models for the car dealership application.

    This module contains the Django model definitions for representing car makes
    and car models. These models define the structure of the data stored in the
    application's database.

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
    year = models.IntegerField(default=2025,
        validators=[
            MaxValueValidator(2025),
            MinValueValidator(2015)
        ])

    def __str__(self):
        return self.name

