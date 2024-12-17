"""
Middleware
This module defines a custom middleware class that enforces profile
completion and handles user redirection based on their approval status.

Middleware:
1. ProfileCompletionMiddleware: Ensures that users are redirected to the
   appropriate pages based on their account's approval status and profile
   completion.

Key Features:
- Unrestricted access for staff and superuser accounts.
- Redirects 'pending' users to the registration pending page.
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

    The middleware evaluates the following conditions for authenticated users:
    1. Staff and superuser accounts are allowed unrestricted access.
    2. Users with 'pending' approval status are redirected to the
       registration pending page.
    3. Users with 'disapproved' status are redirected to the disapproval
       message page.
    4. Users with 'approved' status but incomplete profiles are redirected
       to the profile completion page.

    Args:
        get_response (callable): The next middleware or view in the chain.

    Returns:
        callable: The middleware callable function.
    """

    def __init__(self, get_response):
        """
        Initialize the middleware.

        Args:
            get_response (callable): The next middleware or view in the chain.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Process each request and apply redirection logic based on the user's
        approval status and profile completion status.

        Args:
            request (HttpRequest): The current HTTP request object.

        Returns:
            HttpResponse: The HTTP response to the request, with redirection
            applied if necessary.
        """
        # Check if the user is authenticated
        if request.user.is_authenticated:

            # Allow unrestricted access for staff and superuser accounts
            if request.user.is_staff or request.user.is_superuser:
                return self.get_response(request)

            # Allow access to the logout view
            if request.path == reverse('accounts:account_logout'):
                return self.get_response(request)

            # Redirect users based on their approval status
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
                    reverse('accounts:account_logout'),
                ]
                if request.path not in allowed_paths:
                    return redirect('accounts:complete_profile')

        # Continue to the requested view if no redirect conditions are met
        response = self.get_response(request)
        return response
