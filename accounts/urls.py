from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
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
    # Authentication and account management
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('login/', CustomLoginView.as_view(), name='account_login'),
    path('logout/', CustomLogoutView.as_view(), name='account_logout'),

    # Profile management
    path('complete_profile/', complete_profile, name='complete_profile'),
    path('registration_pending/', registration_pending, name='registration_pending'),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('update_profile/', update_profile, name='update_profile'),

    # Crew profile and user management
    path('profile/<int:user_id>/<int:trip_id>/', crew_profile, name='crew_profile'),
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),

    # Password reset
    path('password/reset/', CustomPasswordResetView.as_view(), name='account_reset_password'),
    path('password/reset/done/', CustomPasswordResetDoneView.as_view(), name='account_reset_password_done'),
    path('password/reset/sent/', TemplateView.as_view(template_name="account/password_reset_sent.html"), name='password_reset_sent'),
    path('password/reset/key/<uidb64>/<token>/', allauth_views.PasswordResetFromKeyView.as_view(), name='account_reset_password_from_key'),
    path('password/reset/key/done/', allauth_views.PasswordResetFromKeyDoneView.as_view(), name='account_reset_password_from_key_done'),

    # Error handling
    path('auth/inactive/', inactive_account_redirect, name='account_inactive'),
]

# Static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
