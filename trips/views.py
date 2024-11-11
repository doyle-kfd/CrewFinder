from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Trip
from .forms import TripCreationForm
from crewbooking.models import CrewBooking

@login_required
def create_trip(request):
    if request.user.role != "captain":
        raise PermissionDenied("Only captains can create trips.")
    
    if request.method == 'POST':
        form = TripCreationForm(request.POST, request.FILES)  # Include request.FILES to handle image uploads
        if form.is_valid():
            trip = form.save(commit=False)
            trip.captain = request.user
            trip.save()
            return redirect('dashboard')
    else:
        form = TripCreationForm()
    
    return render(request, 'trips/create_trip.html', {'form': form})

@login_required
def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, captain=request.user)  # Ensure only the captain can delete

    if request.method == 'POST':
        trip.delete()  # Delete the trip
        return redirect('dashboard')  # Redirect back to the dashboard after deletion
    
    return render(request, 'trips/delete_trip_confirm.html', {'trip': trip})

@login_required
def captain_dashboard(request):
    if request.user.role == "captain":
        my_trips = Trip.objects.filter(captain=request.user).order_by('date')
        
        # Fetch crew bookings related to the trips and pass them along
        applied_crews = CrewBooking.objects.filter(trip__in=my_trips)  # Get CrewBookings for the captain's trips

        return render(request, 'accounts/dashboard.html', {'my_trips': my_trips, 'applied_crews': applied_crews})
    else:
        raise PermissionDenied("Only captains can access this dashboard.")



@login_required
def edit_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, captain=request.user)
    if request.method == 'POST':
        form = TripCreationForm(request.POST, request.FILES, instance=trip)  # Include request.FILES for image updates
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TripCreationForm(instance=trip)
    
    return render(request, 'trips/edit_trip.html', {'form': form, 'trip': trip})
