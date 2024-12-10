"""
Middleware
This module defines a custom middleware class that enforces profile
completion
and handles user redirection based on their approval status.

Middleware:
1. ProfileCompletionMiddleware: Ensures that users are redirected to
   appropriate
   pages depending on their account's approval status and profile completion.

Key Features:
- Unrestricted access for staff and superuser accounts.
- Redirects 'pending' users to a registration pending page.
- Redirects 'disapproved' users to a disapproval message page.
- Redirects 'approved' users with incomplete profiles to the profile
  completion page.

Dependencies:
- Django's `HttpRequest` and `HttpResponse` for request handling.
- Django's URL reversing for redirection logic.
"""

from django.shortcuts import redirect
from django.urls import reverse
from .models import User


class ProfileCompletionMiddleware:
    """
    Middleware to enforce profile completion and handle user redirection
    based on their approval status.

    This middleware checks the following conditions for authenticated users:
    1. Staff and superuser accounts are allowed unrestricted access.
    2. Redirects users with 'pending' status to the registration
       pending page.
    3. Redirects users with 'disapproved' status to a disapproval
       message page.
    4. Redirects users with 'approved' status and incomplete profiles to
       the profile completion page.

    Args:
        get_response (callable): The next middleware or view in the chain.

    Returns:
        callable: The middleware callable function.
    """

    def __init__(self, get_response):
        """
        Initializes the middleware.

        Args:
            get_response (callable): The next middleware or view in the chain.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Processes each request and applies redirection logic based on user
        approval status and profile completion.

        Args:
            request (HttpRequest): The current HTTP request object.

        Returns:
            HttpResponse: The HTTP response to the request, with potential
            redirection applied.
        """
        if request.user.is_authenticated:
            # Allow unrestricted access for staff and superuser accounts
            if request.user.is_staff or request.user.is_superuser:
                return self.get_response(request)

            # Allow access to the logout view
            if request.path == reverse('account_logout'):
                return self.get_response(request)

            # Redirect based on user's approval status
            if request.user.approval_status == User.PENDING:
                if request.path != reverse('registration_pending'):
                    return redirect('registration_pending')
            elif request.user.approval_status == User.DISAPPROVED:
                if request.path != reverse('disapproval_message'):
                    return redirect('disapproval_message')
            elif (
                request.user.approval_status == User.APPROVED and
                not request.user.profile_completed
            ):
                allowed_paths = [
                    reverse('accounts:complete_profile'),
                    reverse('account_logout'),
                ]
                if request.path not in allowed_paths:
                    return redirect('accounts:complete_profile')

        # Continue to the requested view if no redirect condition is met
        response = self.get_response(request)
        return response
