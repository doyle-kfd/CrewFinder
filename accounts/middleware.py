from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user is logged in and profile is incomplete
        if request.user.is_authenticated and not request.user.profile_completed:
            # Redirect to complete profile page if not already there
            if request.path != reverse('complete_profile'):
                return redirect('complete_profile')
        
        response = self.get_response(request)
        return response