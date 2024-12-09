"""
App Configuration
This module defines the application configuration for the `accounts` app,
which manages user authentication, profile management, and role-based access
control. The configuration includes settings and ensures that signals are
registered when the application is ready.

Configuration:
1. AccountsConfig: Configures settings for the accounts application, including
   default field types and the registration of signal handlers.

Key Features:
- Automatic signal registration for user-related events.
- Centralized configuration of app-specific settings.

Dependencies:
- Django's AppConfig class for application settings.
- Signal handlers for user management events.
"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuration class for the accounts application. Handles application
    settings and ensures signals are registered when the app is ready.

    Attributes:
        default_auto_field (str): Specifies the type of auto-generated field
        for primary keys.
        name (str): The name of the application.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        """
        Imports and registers signal handlers for the accounts app.
        This ensures that the signals are active when the application
        starts.
        """
        import accounts.signals
