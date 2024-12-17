"""
Project URL Configuration
This module defines the URL routing for the project, including app-specific
routes and custom error handlers.

Key Features:
1. Admin panel for site administration.
2. App-specific URL configurations for accounts, trips, crew bookings,
   and static pages.
3. Custom error views for improved user experience.
4. Serving media files in development mode.

Dependencies:
- Django's URL routing system.
- Django's admin panel for site administration.
- Custom error views for improved user experience.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler403, handler400, handler500

# -------------------------
# Custom Error Handlers
# -------------------------
handler404 = 'pages.views.custom_404_view'  # 404 Page Not Found handler
handler403 = 'pages.views.custom_403_view'  # 403 Permission Denied handler
handler400 = 'pages.views.custom_400_view'  # 400 Bad Request handler
handler500 = 'pages.views.custom_500_view'  # 500 Server Error handler

# -------------------------
# URL Patterns
# -------------------------
urlpatterns = [
    # Admin panel for site administration
    path('admin/', admin.site.urls),

    # Custom account management URLs
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # Default authentication routes from Django Allauth
    path('accounts/', include('allauth.urls')),

    # Trip-related functionality (creating, managing trips)
    path('trips/', include('trips.urls', namespace='trips')),

    # Static pages such as home, about, contact
    path('', include('pages.urls')),

    # Crew booking functionality (applying, managing crew bookings)
    path('crewbooking/', include('crewbooking.urls')),
]

# -------------------------
# Media Files (Development Mode)
# -------------------------
if settings.DEBUG:
    # Serve media files like images in development mode
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
