from django.shortcuts import redirect
from django.urls import reverse
from .models import User

class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Allow unrestricted access for staff and superuser accounts
            if request.user.is_staff or request.user.is_superuser:
                return self.get_response(request)

            # Redirect users based on their approval status
            if request.user.approval_status == User.PENDING:
                # Redirect pending users to the registration pending page
                if request.path != reverse('registration_pending'):
                    return redirect('registration_pending')
            elif request.user.approval_status == User.DISAPPROVED:
                # Redirect disapproved users to a disapproval message page
                if request.path != reverse('disapproval_message'):
                    return redirect('disapproval_message')

            # If user is approved but profile is incomplete, redirect to profile completion page
            elif request.user.approval_status == User.APPROVED and not request.user.profile_completed:
                # Define allowed paths for profile completion process
                allowed_paths = [
                    reverse('complete_profile'),
                    reverse('logout'),
                ]
                if request.path not in allowed_paths:
                    return redirect('complete_profile')

        # Continue to the requested view if no redirect condition is met
        response = self.get_response(request)
        return response
