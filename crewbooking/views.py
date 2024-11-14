from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages for feedback
from .models import CrewBooking
from trips.models import Trip  # Import your Trip model
from crewbooking.models import CrewBooking  # Make sure to import the CrewBooking model

@login_required
def apply_for_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    
    # Check if the user is already a crew member and has applied
    if CrewBooking.objects.filter(user=request.user, trip=trip).exists():
        # If the user already applied, just return a message or redirect
        return redirect('dashboard')  # Redirect to the dashboard or show a message
    
    # Create a new CrewBooking instance with status 'pending'
    CrewBooking.objects.create(user=request.user, trip=trip, status='pending')
    
    # Redirect back to the dashboard or the trip's page
    return redirect('dashboard')  # Or to the trip's detail page

@login_required
def delete_application(request, booking_id):
    booking = get_object_or_404(CrewBooking, id=booking_id, user=request.user)
    booking.delete()
    return redirect('dashboard')  # Redirect to dashboard after deleting

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