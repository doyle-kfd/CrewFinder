from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages for feedback
from .models import CrewBooking
from trips.models import Trip  # Import your Trip model

@login_required
def apply_for_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)

    # Check if the user has already applied for this trip
    if CrewBooking.objects.filter(user=request.user, trip=trip).exists():
        messages.warning(request, "You have already applied for this trip.")
        return redirect('dashboard')  # Redirect back to the dashboard

    if request.method == 'POST':
        # Create a new CrewBooking entry for the specific trip
        CrewBooking.objects.create(user=request.user, trip=trip, status='pending')
        messages.success(request, "You have successfully applied for the trip.")
        return redirect('dashboard')  # Redirect to dashboard after applying

    return render(request, 'crewbooking/apply_for_trip.html', {'trip': trip})
