""" Flow
    Admin Configuration: Registers models for the Django admin interface, making them manageable through the admin site.

    Flow:
        1. Developer Definition: Developer defines how models from models.py should be displayed and managed in the admin.
        > 2. Current File (admin.py): This file contains the registration of models with Django's admin site.
        3. Django Admin Site: Django's admin interface uses these registrations to build its UI.
        4. Admin User Interaction: Admin users create, read, update, and delete data through this interface, affecting the database via the models.
"""

from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
# CarModelInline class

# CarModelAdmin class
admin.site.register(CarMake)
admin.site.register(CarModel)

# CarMakeAdmin class with CarModelInline

# Register models here
