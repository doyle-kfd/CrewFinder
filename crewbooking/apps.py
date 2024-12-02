"""
App configuration for the crewbooking app.

This module defines the configuration for the crewbooking
app in the CrewFinder project.
The app handles user applications (crew bookings) for trips,
linking users to trips
and tracking their application statuses.

Classes:
- CrewbookingConfig: Configures the crewbooking app for Django.
"""

from django.apps import AppConfig


class CrewbookingConfig(AppConfig):
    """
    Configures the crewbooking app.

    Attributes:
    - default_auto_field (str): Specifies the default primary key
      field type for models
      in this app (`BigAutoField` is used for auto-incrementing
      primary keys).
    - name (str): The name of the app as defined in the project.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crewbooking'
