from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.CustomSignupView.as_view(), name='account_signup'),  # Custom signup view
    path('', include('allauth.urls')),  # Include the remaining Allauth URLs
    path('complete_profile/', views.complete_profile, name='complete_profile'),
    path('registration_pending/', views.registration_pending, name='registration_pending'),
    path('dashboard/', views.dashboard, name='dashboard'),
]