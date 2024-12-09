"""
URL Configuration
This module defines the URL patterns for the authentication system, leveraging 
Django Allauth views to handle login and signup functionalities. It provides a 
centralized routing mechanism for account-related actions.

URL Patterns:
1. Login: Maps to Django Allauth's LoginView for user authentication.
2. Signup: Maps to Django Allauth's SignupView for user registration.

Key Features:
- Clean and extendable URL routing for authentication.
- Integration with Django Allauth for robust user management.

Dependencies:
- Django's URL dispatcher.
- Django Allauth views for handling authentication and signup processes.
"""

from allauth.account import views as allauth_views
from django.urls import path

urlpatterns = [
    path('login/', allauth_views.LoginView.as_view(), name='account_login'),
    path('signup/', allauth_views.SignupView.as_view(), name='account_signup'),
    # Exclude the logout URL
]
