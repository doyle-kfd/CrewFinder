# accounts/middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Exclude staff or superuser accounts from bio completion requirement
            if request.user.is_staff or request.user.is_superuser:
                return self.get_response(request)

            # Redirect unapproved users (is_active=False) to registration_pending
            if not request.user.is_active:
                return redirect('registration_pending')

            # If user is approved but profile is incomplete, redirect to complete_profile
            elif not request.user.profile_completed:
                allowed_paths = [
                    reverse('complete_profile'),
                    reverse('logout'),
                ]
                if request.path not in allowed_paths:
                    return redirect('complete_profile')

        response = self.get_response(request)
        return response