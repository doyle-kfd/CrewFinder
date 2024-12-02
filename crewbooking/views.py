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
    - request: The HTTP request object.
    - trip_id: The ID of the trip the user wants to apply for.

    Process:
    1. Retrieves the trip object based on `trip_id`.
    2. Checks if the user has already applied for the trip.
    3. If not, creates a new `CrewBooking` instance with status 'pending'.
    4. Redirects the user to their dashboard.

    Returns:
    - HTTP response redirecting to the dashboard.
    """
    trip = get_object_or_404(Trip, id=trip_id)

    # Check if the user is already a crew member and has applied
    if CrewBooking.objects.filter(user=request.user, trip=trip).exists():
        # If the user already applied, just return a message or redirect
        # Redirect to the dashboard or show a message
        return redirect('dashboard')

    # Create a new CrewBooking instance with status 'pending'
    CrewBooking.objects.create(user=request.user, trip=trip, status='pending')

    # Redirect back to the dashboard or the trip's page
    return redirect('dashboard')  # Or to the trip's detail page


@login_required
def delete_application(request, booking_id):
    """
    Allows an authenticated user to delete their application for a trip.

    Parameters:
    - request: The HTTP request object.
    - booking_id: The ID of the booking to delete.

    Process:
    1. Retrieves the booking object based on `booking_id` and user.
    2. Deletes the booking if it exists.
    3. Redirects the user to their dashboard.

    Returns:
    - HTTP response redirecting to the dashboard.
    """
    booking = get_object_or_404(CrewBooking, id=booking_id, user=request.user)
    booking.delete()
    return redirect('dashboard')  # Redirect to dashboard after deleting


def home(request):
    """
    Renders the home page and displays the latest trips.

    Parameters:
    - request: The HTTP request object.

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
    - request: The HTTP request object.

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
