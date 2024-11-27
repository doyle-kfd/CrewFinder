from allauth.account import views as allauth_views
from django.urls import path

urlpatterns = [
    path('login/', allauth_views.LoginView.as_view(), name='account_login'),
    path('signup/', allauth_views.SignupView.as_view(), name='account_signup'),
    # Exclude the logout URL
]