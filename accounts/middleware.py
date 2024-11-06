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

            # Redirect users with "Pending" or "Disapproved" status to the appropriate pages
            if request.user.approval_status == User.PENDING:
                return redirect('registration_pending')
            elif request.user.approval_status == User.DISAPPROVED:
                return redirect('disapproval_message')  # Ensure 'disapproval_message' view and URL are defined

            # If user is "Approved" but profile is incomplete, redirect to profile completion page
            elif request.user.approval_status == User.APPROVED and not request.user.profile_completed:
                allowed_paths = [
                    reverse('complete_profile'),
                    reverse('logout'),
                ]
                if request.path not in allowed_paths:
                    return redirect('complete_profile')

        response = self.get_response(request)
        return response
