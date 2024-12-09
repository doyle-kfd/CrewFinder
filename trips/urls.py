"""
URL configuration for the 'trips' app.

This module defines URL patterns for managing trips in the CrewFinder
application.
Each route is associated with a specific view function that handles
trip-related operations.

Routes:
- create/ : Allows captains to create new trips.
- captain-dashboard/ : Displays the captain's dashboard with their trips
  and crew applications.
- edit/<int:trip_id>/ : Allows captains to edit the details of a
  specific trip.
- delete/<int:trip_id>/ : Allows captains to delete a specific
  trip after confirmation.
"""

from django.urls import path
from . import views

# Namespace for the trips app
app_name = 'trips'

# URL patterns
urlpatterns = [
    # Route for creating new trips
    path('create/', views.create_trip, name='create_trip'),

    # Route for the captain's dashboard
    path('captain-dashboard/', views.captain_dashboard,
         name='captain_dashboard'),

    # Route for editing a trip
    path('edit/<int:trip_id>/', views.edit_trip, name='edit_trip'),

    # Route for deleting a trip
    path('delete/<int:trip_id>/', views.delete_trip, name='delete_trip'),
]
