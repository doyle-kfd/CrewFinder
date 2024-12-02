"""
Views for managing trips in the CrewFinder application.

This module provides views for captains to create, edit, delete,
and manage their trips.
It includes permission checks to ensure only captains can perform
these actions.

Functions:
- create_trip: Allows captains to create new trips.
- captain_dashboard: Displays a dashboard for captains with their trips
  and crew applications.
- edit_trip: Allows captains to edit the details of their existing trips.
- delete_trip: Allows captains to delete their trips with a confirmation step.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Trip
from .forms import TripCreationForm
from crewbooking.models import CrewBooking


@login_required
def create_trip(request):
    """
    Allows captains to create new trips.

    Parameters:
    - request: The HTTP request object.

    Process:
    1. Checks if the logged-in user has the "captain" role.
    2. Handles form submission for trip creation.
    3. Saves the trip if the form is valid and redirects to
       the captain's dashboard.

    Returns:
    - Rendered HTML form for creating a new trip.
    - Redirect to the dashboard upon successful trip creation.

    Raises:
    - PermissionDenied: If the user is not a captain.
    """
    if request.user.role != "captain":
        raise PermissionDenied("Only captains can create trips.")

    if request.method == 'POST':
        # Include request.FILES for image uploads
        form = TripCreationForm(request.POST, request.FILES)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.captain = request.user
            trip.save()
            return redirect('accounts:dashboard')
    else:
        form = TripCreationForm()

    return render(request, 'trips/create_trip.html',
                  {'form': form})


@login_required
def captain_dashboard(request):
    """
    Displays the captain's dashboard with their trips and crew applications.

    Parameters:
    - request: The HTTP request object.

    Process:
    1. Checks if the logged-in user is a captain.
    2. Retrieves all trips created by the captain.
    3. Retrieves all crew applications for the captain's trips.

    Returns:
    - Rendered captain's dashboard with trip and crew application details.

    Raises:
    - PermissionDenied: If the user is not a captain.
    """
    if request.user.role == "captain":
        my_trips = Trip.objects.filter(captain=request.user). order_by(
            'departure_date')
        applied_crews = CrewBooking.objects.filter(trip__in=my_trips)

        return render(request, 'accounts/dashboard.html',
                      {'my_trips': my_trips,   'applied_crews':
                          applied_crews})
    else:
        raise PermissionDenied("Only captains can access this dashboard.")


@login_required
def edit_trip(request, trip_id):
    """
    Allows captains to edit the details of an existing trip.

    Parameters:
    - request: The HTTP request object.
    - trip_id: The ID of the trip to edit.

    Process:
    1. Fetches the trip object and ensures the user is its captain.
    2. Handles form submission for trip editing.
    3. Saves the changes if the form is valid and redirects to the
       captain's dashboard.

    Returns:
    - Rendered HTML form for editing the trip.
    - Redirect to the dashboard upon successful trip editing.

    Raises:
    - PermissionDenied: If the user is not the captain of the trip.
    """
    trip = get_object_or_404(Trip, id=trip_id, captain=request.user)
    if request.method == 'POST':
        form = TripCreationForm(request.POST, request.FILES, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('accounts:dashboard')
    else:
        form = TripCreationForm(instance=trip)

    return render(request, 'trips/edit_trip.html',
                  {'form': form, 'trip': trip})


@login_required
def delete_trip(request, trip_id):
    """
    Allows captains to delete a trip with a confirmation step.

    Parameters:
    - request: The HTTP request object.
    - trip_id: The ID of the trip to delete.

    Process:
    1. Fetches the trip object and ensures the user is its captain.
    2. Deletes the trip if the request method is POST.
    3. Redirects to the captain's dashboard after successful deletion.

    Returns:
    - Rendered confirmation page for trip deletion.
    - Redirect to the dashboard upon successful deletion.

    Raises:
    - PermissionDenied: If the user is not the captain of the trip.
    """
    trip = get_object_or_404(Trip, id=trip_id, captain=request.user)
    if request.method == 'POST':
        trip.delete()
        return redirect('accounts:dashboard')
    return render(request, 'trips/delete_trip_confirm.html',
                  {'trip': trip})
