from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.CustomSignupView.as_view(), name='account_signup'),  # Custom signup view
    path('login/', views.CustomLoginView.as_view(), name='account_login'),     # Custom login view to handle role-based redirection
    path('', include('allauth.urls')),  # Include the remaining Allauth URLs
    path('complete_profile/', views.complete_profile, name='complete_profile'),  # Profile completion
    path('registration_pending/', views.registration_pending, name='registration_pending'),  # Pending registration
    path('dashboard/', views.dashboard, name='dashboard'),  # Default dashboard
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Admin dashboard for Administrator role
]