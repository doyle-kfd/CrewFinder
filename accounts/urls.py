from django.urls import path, include
from . import views  # Import views from the current directory
from django.conf.urls.static import static
from django.conf import settings 
from .views import (
    CustomSignupView,
    CustomLoginView,
    CustomLogoutView,
    complete_profile,
    update_profile,
    registration_pending,
    dashboard,
    admin_dashboard
)

urlpatterns = [
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('login/', CustomLoginView.as_view(), name='account_login'),
    path('logout/', CustomLogoutView.as_view(), name='account_logout'),
    path('complete_profile/', complete_profile, name='complete_profile'),
    path('registration_pending/', registration_pending, name='registration_pending'),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('', include('allauth.urls')),  # Include the remaining Allauth URLs
    path('update_profile/', update_profile, name='update_profile'),  # New profile update URL
    path('profile/<int:user_id>/', views.crew_profile, name='crew_profile'), # Crewmembers profile
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
