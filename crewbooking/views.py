from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages for feedback
from .models import CrewBooking
from trips.models import Trip  # Import your Trip model
from crewbooking.models import CrewBooking  # Make sure to import the CrewBooking model

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

def home(request):
    # Fetch the latest three trips to display on the home page
    trips = Trip.objects.order_by('-date')[:3]

    # If the user is authenticated, fetch applied trip IDs
    if request.user.is_authenticated:
        applied_trip_ids = CrewBooking.objects.filter(user=request.user).values_list('trip_id', flat=True)
    else:
        applied_trip_ids = []

    return render(request, 'pages/home.html', {
        'trips': trips,
        'applied_trip_ids': applied_trip_ids,
    })

def sailing_opportunities(request):
    # Fetch all trips
    trips = Trip.objects.all()  # This line should retrieve all trips

    # If the user is authenticated, fetch applied trip IDs
    if request.user.is_authenticated:
        applied_trip_ids = CrewBooking.objects.filter(user=request.user).values_list('trip_id', flat=True)
    else:
        applied_trip_ids = []

    return render(request, 'pages/sailing_opportunities.html', {
        'trips': trips,
        'applied_trip_ids': applied_trip_ids,
    })