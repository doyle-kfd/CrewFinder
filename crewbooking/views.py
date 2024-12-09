"""
Views
This module defines views for handling user interactions,
including applying for trips,
deleting applications, and displaying static pages such as the home and
Sailing Opportunities pages.

View Functions:
1. apply_for_trip: Allows users to apply for a specific trip.
2. delete_application: Enables users to delete their trip applications.
3. home: Displays the home page with the latest trips.
4. sailing_opportunities: Lists all available trips on the Sailing
   Opportunities page.

Key Features:
- Authentication checks for actions like applying for or deleting trip
applications.
- Integration with the CrewBooking model for managing user-trip relationships.
- Dynamic display of trips and user application statuses.

Dependencies:
- Django's shortcuts for rendering and model retrieval.
- Django's authentication decorators for login-required views.
- Models for trips and crew bookings.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages for feedback
from .models import CrewBooking
from trips.models import Trip  # Import your Trip model
# Make sure to import the CrewBooking model
from crewbooking.models import CrewBooking


@login_required
def apply_for_trip(request, trip_id):
    """
    Allows an authenticated user to apply for a specific trip.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - trip_id (int): The ID of the trip the user wants to apply for.

    Process:
    1. Checks if the trip exists and retrieves it.
    2. Verifies if the user has already applied for the trip.
    3. Creates a new CrewBooking instance with the status set to 'pending.'
    4. Redirects the user back to their dashboard.

    Returns:
    - HttpResponseRedirect: Redirects to the user's dashboard.
    """
    trip = get_object_or_404(Trip, id=trip_id)

    # Check if the user has already applied for the trip
    if CrewBooking.objects.filter(user=request.user, trip=trip).exists():
        # Redirect to the dashboard with a message if already applied
        # Use the correct namespace for the dashboard
        return redirect('accounts:dashboard')

    # Create a new CrewBooking instance with status 'pending'
    CrewBooking.objects.create(user=request.user, trip=trip, status='pending')

    # Redirect back to the user's dashboard
    return redirect('accounts:dashboard')  # Corrected namespace


@login_required
def delete_application(request, booking_id):
    """
    Allows an authenticated user to delete their application for a trip.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - booking_id (int): The ID of the CrewBooking record to be deleted.

    Process:
    1. Retrieves the CrewBooking instance for the user and trip.
    2. Deletes the application record.
    3. Redirects the user back to their dashboard.

    Returns:
    - HttpResponseRedirect: Redirects to the user's dashboard.
    """
    booking = get_object_or_404(CrewBooking, id=booking_id, user=request.user)
    booking.delete()

    # Redirect to the user's dashboard after deleting the application
    return redirect('accounts:dashboard')  # Corrected namespace


def home(request):
    """
    Renders the home page and displays the latest trips.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Process:
    1. Fetches the latest three trips ordered by date.
    2. If the user is authenticated,
       retrieves the IDs of trips the user has applied for.
    3. Renders the home page template with the trips and applied trip IDs.

    Returns:
    - Rendered HTML response for the home page.
    """
    # Fetch the latest three trips to display on the home page
    trips = Trip.objects.order_by('-date')[:3]

    # If the user is authenticated, fetch applied trip IDs
    if request.user.is_authenticated:
        applied_trip_ids = (CrewBooking.objects.filter(user=request.user).
                            values_list('trip_id', flat=True))
    else:
        applied_trip_ids = []

    return render(request, 'pages/home.html', {
        'trips': trips,
        'applied_trip_ids': applied_trip_ids,
    })


def sailing_opportunities(request):
    """
    Renders the Sailing Opportunities page and lists all trips.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Process:
    1. Fetches all trips from the database.
    2. If the user is authenticated, retrieves the IDs of trips
       the user has applied for.
    3. Renders the Sailing Opportunities page template with the trips
       and applied trip IDs.

    Returns:
    - Rendered HTML response for the Sailing Opportunities page.
    """
    # Fetch all trips
    trips = Trip.objects.all()  # This line should retrieve all trips

    # If the user is authenticated, fetch applied trip IDs
    if request.user.is_authenticated:
        applied_trip_ids = (CrewBooking.objects.filter(user=request.user).
                            values_list('trip_id', flat=True))
    else:
        applied_trip_ids = []

    return render(request, 'pages/sailing_opportunities.html',
                  {'trips': trips,
                   'applied_trip_ids': applied_trip_ids,
                   })
