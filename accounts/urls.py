from django.urls import path, include
from . import views

urlpatterns = [ 
    # Include all of Allauth’s default URLs for login, signup, logout, etc.
    path('', include('allauth.urls')),
    # Custom URL for profile completion, pointing to your custom view
    path('complete_profile/', views.complete_profile, name='complete_profile'),
]