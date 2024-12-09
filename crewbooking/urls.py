"""
URL Configuration
This module defines the URL patterns for the `crewbooking` app,
enabling functionality 
for users to apply for trips and delete their trip applications.

URL Patterns:
1. apply_for_trip: Maps to the view that allows users to apply for a trip
   using the trip's ID.
2. delete_application: Maps to the view that allows users to delete their trip 
   application using the booking ID.

Key Features:
- Dynamic URL routing for trip applications and deletions.
- Namespaced URL patterns for easy reference and maintainability.

Dependencies:
- Django's URL dispatcher for routing.
- Views from the `crewbooking` app for handling user actions.
"""

from django.urls import path
from django.urls import include
from . import views

app_name = 'crewbooking'

urlpatterns = [
    path('apply/<int:trip_id>/', views.apply_for_trip, name='apply_for_trip'),
    path('delete_application/<int:booking_id>/',
         views.delete_application, name='delete_application'),
]
