from django.urls import path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
)
from allauth.account.views import (
    PasswordResetFromKeyView,
    PasswordResetFromKeyDoneView,
)
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
    CustomPasswordResetConfirmView,
)

app_name = 'accounts'

urlpatterns = [
    # Authentication URLs
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('login/', CustomLoginView.as_view(), name='account_login'),
    path('logout/', CustomLogoutView.as_view(), name='account_logout'),

    # Profile Management
    path('complete-profile/', complete_profile, name='complete_profile'),
    path('update_profile/', update_profile, name='update_profile'),

    # Dashboard Views
    path('dashboard/', dashboard, name='dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),

    # User Management
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path('profile/<int:user_id>/<int:trip_id>/', crew_profile, name='crew_profile'),

    # Password Management
    path('password/reset/', CustomPasswordResetView.as_view(), name='account_reset_password'),
    path('password/reset/done/', CustomPasswordResetDoneView.as_view(), name='account_reset_password_done'),
    path('password/reset/key/<uidb36>/<key>/', PasswordResetFromKeyView.as_view(), name='account_reset_password_from_key'),
    path('password/reset/key/done/', PasswordResetFromKeyDoneView.as_view(), name='account_reset_password_from_key_done'),
    path('password/reset/sent/', TemplateView.as_view(template_name="account/password_reset_sent.html"), name='password_reset_sent'),
    path(
        'password/change/',
        PasswordChangeView.as_view(
            template_name='account/password_change_form.html',
            success_url=reverse_lazy('accounts:password_change_done')
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

    # Registration Pending and Inactive Redirect
    path('registration_pending/', registration_pending, name='registration_pending'),
    path('auth/inactive/', inactive_account_redirect, name='account_inactive'),
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
