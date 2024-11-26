from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse


class CustomAccountAdapter(DefaultAccountAdapter):
    """
    Custom adapter to modify Allauth behavior for account redirection and
    login logic.

    Methods:
        get_signup_redirect_url(request): Redirects users to the
        registration pending page after signup.
        get_login_redirect_url(request): Redirects inactive users to the
        registration pending page instead of the default inactive page.
        login(request, user): Prevents auto-login for new users by checking
        their `is_active` status.
    """

    def get_signup_redirect_url(self, request):
        """
        Redirects users to the registration pending page after successful
        signup.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            str: The URL for the registration pending page.
        """
        return reverse('registration_pending')

    def get_login_redirect_url(self, request):
        """
        Redirects inactive users to the registration pending page instead of
        the default inactive page.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            str: The URL for the appropriate login redirection.
        """
        user = request.user
        if not user.is_active:
            return reverse('registration_pending')
        return super().get_login_redirect_url(request)

    def login(self, request, user):
        """
        Overrides the default login behavior to prevent auto-login for
        inactive users.

        Args:
            request (HttpRequest): The HTTP request object.
            user (User): The user instance being logged in.

        Returns:
            None
        """
        if user.is_active:
            super().login(request, user)
