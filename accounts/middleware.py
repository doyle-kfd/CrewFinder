from django.shortcuts import redirect
from django.urls import reverse
from .models import User

class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only proceed if the user is authenticated
        if request.user.is_authenticated:
            # Allow unrestricted access for staff and superuser accounts
            if request.user.is_staff or request.user.is_superuser:
                return self.get_response(request)

            # Check if the request is for the logout view to allow users to log out without redirection
            if request.path == reverse('account_logout'):
                return self.get_response(request)

            # Redirect based on user's approval status
            if request.user.approval_status == User.PENDING:
                if request.path != reverse('registration_pending'):
                    return redirect('registration_pending')
            elif request.user.approval_status == User.DISAPPROVED:
                if request.path != reverse('disapproval_message'):
                    return redirect('disapproval_message')
            elif request.user.approval_status == User.APPROVED and not request.user.profile_completed:
                allowed_paths = [
                    reverse('complete_profile'),
                    reverse('account_logout'),
                ]
                if request.path not in allowed_paths:
                    return redirect('complete_profile')

        # Continue to the requested view if no redirect condition is met
        response = self.get_response(request)
        return response
