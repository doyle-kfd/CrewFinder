from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from .models import CrewBooking
from trips.models import Trip
from django.contrib.auth.decorators import login_required

@login_required
def apply_for_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)

    if request.user.role != "crew":
        return render(request, 'crewbooking/access_denied.html')  # Handle access denied

    if request.method == 'POST':
        # Create a new booking for the trip
        CrewBooking.objects.create(trip=trip, user=request.user, status='pending')
        return redirect('dashboard')  # Redirect to dashboard or another appropriate page

    # For GET requests, just render the trip details
    return render(request, 'crewbooking/apply_for_trip.html', {'trip': trip})