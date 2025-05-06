from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
# - Any other fields you would like to include in car make model
class CarMake(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    # - __str__ method to print a car make object
    def __str__(self):
        return self.name 



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    # - Many-To-One relationship to Car Make model (One Car Make has many
    # Car Models, using ForeignKey field)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    # - Type (CharField with a choices argument to provide limited choices
    # such as Sedan, SUV, WAGON, etc.)
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
    # - Any other fields you would like to include in car model
    # - __str__ method to print a car make object
    def __str__(self):
        return self.name

