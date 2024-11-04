from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_signup_redirect_url(self, request):
        redirect_url = reverse('registration_pending')
        print("Custom adapter loaded!")  # This should appear in the console when the adapter is used
        return redirect_url