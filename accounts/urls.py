from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
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

urlpatterns = [
    # Authentication and account management URLs
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('login/', CustomLoginView.as_view(), name='account_login'),
    path('logout/', CustomLogoutView.as_view(), name='account_logout'),

    # Profile-related URLs
    path('complete_profile/', complete_profile, name='complete_profile'),
    path(
        'registration_pending/',
        registration_pending,
        name='registration_pending'
    ),
    path('dashboard/', dashboard, name='dashboard'),
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

    # Include remaining Allauth URLs
    path('', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
