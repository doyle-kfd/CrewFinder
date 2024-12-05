from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import inactive_account_redirect
from . import views

from .views import (
    CustomSignupView,
    CustomLoginView,
    CustomLogoutView,
    complete_profile,
    update_profile,
    registration_pending,
    dashboard,
    admin_dashboard,
)

# Import Allauth URLs but exclude the signup view
from allauth.account import views as allauth_views

app_name = 'accounts'

urlpatterns = [
    # Authentication and account management URLs
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('login/', CustomLoginView.as_view(), name='account_login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Custom LogoutView

    # Profile-related URLs
    path('complete_profile/', complete_profile, name='complete_profile'),
    path(
        'registration_pending/',
        registration_pending,
        name='registration_pending'
    ),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('update_profile/', update_profile, name='update_profile'),

    # Crew profile and user management URLs
    path(
        'profile/<int:user_id>/<int:trip_id>/',
        views.crew_profile,
        name='crew_profile'
    ),
    path(
        'edit_user/<int:user_id>/',
        views.edit_user,
        name='edit_user'
    ),

    path('auth/inactive/', inactive_account_redirect, name='account_inactive'),



    # Include remaining Allauth URLs except signup and logout
    path('auth/login/', allauth_views.LoginView.as_view(), name='account_login'),
    # Exclude allauth's signup and logout views
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
