"""
Account URLs
This module defines the URL patterns for the 'accounts' app. It includes
paths for authentication, password reset, profile management, and dashboards.

Dependencies:
- Django's built-in authentication views for password management.
- Custom views for account management and user-specific functionality.
"""

from django.urls import path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
)
from .views import (
    CustomSignupView,
    CustomLoginView,
    CustomLogoutView,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
    complete_profile,
    update_profile,
    registration_pending,
    dashboard,
    admin_dashboard,
    inactive_account_redirect,
    crew_profile,
    edit_user,
)

app_name = 'accounts'

urlpatterns = [
    # -------------------------
    # Password Reset URLs
    # -------------------------
    path(
        'password/reset/',
        CustomPasswordResetView.as_view(
            template_name='account/password_reset.html',
            email_template_name='account/password_reset_email.html',
            success_url=reverse_lazy('accounts:account_reset_password_done'),
        ),
        name='account_reset_password',
    ),
    path(
        'password/reset/done/',
        CustomPasswordResetDoneView.as_view(
            template_name='account/password_reset_done.html'
        ),
        name='account_reset_password_done',
    ),
    path(
        'password/reset/confirm/<uidb64>/<token>/',
        CustomPasswordResetConfirmView.as_view(
            template_name='account/password_reset_confirm.html',
            success_url=reverse_lazy('accounts:password_reset_complete'),
        ),
        name='password_reset_confirm',
    ),
    path(
        'password/reset/key/done/',
        CustomPasswordResetCompleteView.as_view(
            template_name='account/password_reset_complete.html'
        ),
        name='account_reset_password_complete',
    ),
    path(
        'password/reset/complete/',
        CustomPasswordResetCompleteView.as_view(
            template_name='account/password_reset_complete.html'
        ),
        name='password_reset_complete',  # Default name
    ),

    # -------------------------
    # Authentication URLs
    # -------------------------
    path(
        'signup/',
        CustomSignupView.as_view(),
        name='account_signup',
    ),
    path(
        'login/',
        CustomLoginView.as_view(),
        name='account_login',
    ),
    path(
        'logout/',
        CustomLogoutView.as_view(),
        name='account_logout',
    ),

    # -------------------------
    # Profile Management
    # -------------------------
    path(
        'complete-profile/',
        complete_profile,
        name='complete_profile',
    ),
    path(
        'update_profile/',
        update_profile,
        name='update_profile',
    ),

    # -------------------------
    # Dashboard Views
    # -------------------------
    path(
        'dashboard/',
        dashboard,
        name='dashboard',
    ),
    path(
        'admin_dashboard/',
        admin_dashboard,
        name='admin_dashboard',
    ),

    # -------------------------
    # User Management
    # -------------------------
    path(
        'edit_user/<int:user_id>/',
        edit_user,
        name='edit_user',
    ),
    path(
        'profile/<int:user_id>/<int:trip_id>/',
        crew_profile,
        name='crew_profile',
    ),

    # -------------------------
    # Password Change URLs
    # -------------------------
    path(
        'password/change/',
        PasswordChangeView.as_view(
            template_name='account/password_change_form.html',
            success_url=reverse_lazy('accounts:password_change_done'),
        ),
        name='password_change',
    ),
    path(
        'password/change/done/',
        PasswordChangeDoneView.as_view(
            template_name='account/password_change_done.html'
        ),
        name='password_change_done',
    ),

    # -------------------------
    # Registration and Inactive Redirects
    # -------------------------
    path(
        'registration_pending/',
        registration_pending,
        name='registration_pending',
    ),
    path(
        'auth/inactive/',
        inactive_account_redirect,
        name='account_inactive',
    ),
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
