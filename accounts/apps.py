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
