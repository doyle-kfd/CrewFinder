"""
URLs configuration for the Accounts application.

This module defines the URL patterns for the Accounts app, which includes
authentication, profile management, user dashboards, administrative functions,
and password management. These URLs route requests to corresponding views.
"""

from django.urls import path, reverse_lazy
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView
)
from allauth.account import views as allauth_views
from .views import (
    CustomSignupView,
    CustomLoginView,
    CustomLogoutView,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
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
    # Handles user registration using a custom signup form.
    path('signup/', CustomSignupView.as_view(), name='account_signup'),

    # Handles user login with a custom login view.
    path('login/', CustomLoginView.as_view(), name='account_login'),

    # Handles user logout and redirects to the home page.
    path('logout/', CustomLogoutView.as_view(), name='account_logout'),

    # Allows users to complete their profile after registration.
    path('complete-profile/', views.complete_profile, name='complete_profile'),

    # Displays a page for users awaiting admin approval.
    path('registration_pending/', registration_pending, name='registration_pending'),

    # Renders the user dashboard based on the user's role.
    path('dashboard/', dashboard, name='dashboard'),

    # Displays a dashboard for administrators to manage user accounts.
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),

    # Allows users to update their profile details.
    path('update_profile/', update_profile, name='update_profile'),

    # Allows captains to view and manage crew applications for trips.
    path('profile/<int:user_id>/<int:trip_id>/', crew_profile, name='crew_profile'),

    # Allows administrators to edit user details such as roles.
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),

    # Handles user password reset requests using a custom view.
    path('password/reset/', CustomPasswordResetView.as_view(), name='account_reset_password'),

    # Displays a confirmation page after requesting a password reset.
    path('password/reset/done/', CustomPasswordResetDoneView.as_view(), name='account_reset_password_done'),

    # Displays a confirmation message after sending a password reset email.
    path('password/reset/sent/', TemplateView.as_view(template_name="account/password_reset_sent.html"), name='password_reset_sent'),

    # Handles password reset using a token sent via email.
    path('password/reset/key/<uidb64>/<token>/', allauth_views.PasswordResetFromKeyView.as_view(), name='account_reset_password_from_key'),

    # Displays a confirmation page after completing a password reset.
    path('password/reset/key/done/', allauth_views.PasswordResetFromKeyDoneView.as_view(), name='account_reset_password_from_key_done'),

    # Allows authenticated users to change their password.
    path(
        'password/change/',
        PasswordChangeView.as_view(
            template_name='account/password_change_form.html',
            success_url=reverse_lazy('accounts:password_change_done')
        ),
        name='password_change',
    ),

    # Displays a success page after changing the password.
    path(
        'password/change/done/',
        PasswordChangeDoneView.as_view(
            template_name='account/password_change_done.html'
        ),
        name='password_change_done',
    ),

    # Redirects inactive users to the registration pending page.
    path('auth/inactive/', inactive_account_redirect, name='account_inactive'),
]

# Serves media files in development when DEBUG is enabled.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
