from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse
from django.shortcuts import redirect

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_signup_redirect_url(self, request):
        # Redirect to registration_pending after signup
        return reverse('registration_pending')

    def get_login_redirect_url(self, request):
        # Redirect inactive users to registration_pending instead of inactive page
        user = request.user
        if not user.is_active:
            return reverse('registration_pending')
        return super().get_login_redirect_url(request)

    def login(self, request, user):
        # Prevent auto-login for new users by checking is_active
        if user.is_active:
            super().login(request, user)