"""
This module defines the configuration for the 'pages' app.

The `PagesConfig` class inherits from Django's `AppConfig` and specifies
the default settings for the 'pages' application, including the default
primary key field type and the app's name.

Classes:
    PagesConfig: Configuration class for the 'pages' app.
"""
from django.apps import AppConfig


class PagesConfig(AppConfig):
    """
    Configuration class for the 'pages' app.

    Attributes:
        default_auto_field (str): Specifies the default type of primary
                                  key field for models in this app.
        name (str): The name of the application,
                    used by Django to identify it.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
