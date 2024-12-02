"""
URL configuration for the CrewFinder project.

This module defines the URL routing for the project.
The `urlpatterns` list directs HTTP requests to the appropriate views.


Key functionalities:
1. Route HTTP requests to views defined in various apps.
2. Handle static and media files in development mode.
3. Define custom error handlers for common HTTP errors.
4. Integrate third-party authentication (Django Allauth)
 and custom account management.

Example URL patterns:
    - Function-based views:
        from my_app import views
        urlpatterns = [path('', views.home, name='home')]
    - Class-based views:
        from other_app.views import Home
        urlpatterns = [path('', Home.as_view(), name='home')]
    - Including other URL configurations:
        from django.urls import include
        urlpatterns = [path('blog/', include('blog.urls'))]
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from accounts.views import CustomLogoutView
from django.conf.urls import handler404, handler403, handler400, handler500
from pages import views as pages_views

# Custom error handlers
# Handles 404 errors (Page Not Found)
handler404 = 'pages.views.custom_404_view'
# Handles 403 errors (Permission Denied)
handler403 = 'pages.views.custom_403_view'
# Handles 400 errors (Bad Request)
handler400 = 'pages.views.custom_400_view'
# Handles 500 errors (Server Error)
handler500 = 'pages.views.custom_500_view'

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel for site administration
    path('accounts/login/',  auth_views.LoginView.as_view(
        template_name='account/login.html'), name='login'),
    # Login page using custom template
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    # Custom logout view to override default behavior
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # Include URLs from the accounts app for user management
    path('accounts/auth/', include('allauth.urls')),
    # Third-party authentication via Django Allauth
    path('trips/', include('trips.urls', namespace='trips')),
    # Include URLs from the trips app for managing sailing trips
    path('', include('pages.urls')),
    # Main static pages like home, about, and contact
    path('crewbooking/', include('crewbooking.urls')),
    # Include URLs for crew booking functionality
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
