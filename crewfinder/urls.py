from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from accounts.views import CustomLogoutView
from django.conf.urls import handler404, handler403, handler400, handler500

# Custom error handlers
handler404 = 'pages.views.custom_404_view'
handler403 = 'pages.views.custom_403_view'
handler400 = 'pages.views.custom_400_view'
handler500 = 'pages.views.custom_500_view'

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel for site administration
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='account/login.html'), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),  # Allauth default routes
    path('accounts/custom/', include('accounts.urls', namespace='accounts')),  # Custom account management
    path('trips/', include('trips.urls', namespace='trips')),  # Trips management
    path('', include('pages.urls')),  # Static pages
    path('crewbooking/', include('crewbooking.urls')),  # Crew booking functionality
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
