"""
App configuration for the trips app.

This module defines the configuration for the trips app in the
CrewFinder project.
The trips app handles the creation, management, and display of sailing trips
within the application.

Classes:
- TripsConfig: Configures the trips app for use in the Django project.
"""

from django.apps import AppConfig


class TripsConfig(AppConfig):
    """
    Configures the trips app.

    Attributes:
    - default_auto_field (str): Specifies the default primary
      key field type for models
      in this app (`BigAutoField` is used for auto-incrementing primary keys).
    - name (str): The name of the app as defined in the project (`'trips'`).
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trips'
