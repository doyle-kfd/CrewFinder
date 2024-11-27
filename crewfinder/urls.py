"""
URL configuration for crewfinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from accounts.views import CustomLogoutView
from django.conf.urls import handler404
from django.conf.urls import handler403
from django.conf.urls import handler400
from django.conf.urls import handler500
from pages import views as pages_views

handler404 = 'pages.views.custom_404_view'
handler403 = 'pages.views.custom_403_view'
handler400 = 'pages.views.custom_400_view'
handler500 = 'pages.views.custom_500_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),  # Direct login template
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),  # Custom logout
    path('accounts/', include('accounts.urls', namespace='accounts')),  # Include custom accounts app URLs
    path('accounts/auth/', include('allauth.urls')),  # Allauth URLs for authentication
    path('trips/', include('trips.urls', namespace='trips')),  # Trips URLs
    path('', include('pages.urls')),  # Main pages (home, about, etc.)
    path('crewbooking/', include('crewbooking.urls')),  # Include crewbooking URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

