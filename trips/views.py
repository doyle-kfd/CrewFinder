from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Trip
from .forms import TripCreationForm

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
            return redirect('captain_dashboard')
    else:
        form = TripCreationForm()
    
    return render(request, 'trips/create_trip.html', {'form': form})

@login_required
def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, captain=request.user)  # Ensure only the captain can delete

    if request.method == 'POST':
        trip.delete()  # Delete the trip
        return redirect('captain_dashboard')  # Redirect back to the dashboard after deletion
    
    return render(request, 'trips/delete_trip_confirm.html', {'trip': trip})

@login_required
def captain_dashboard(request):
    if request.user.role == "captain":
        # Retrieve trips created by the logged-in captain, sorted by date
        my_trips = Trip.objects.filter(captain=request.user).order_by('date')
        return render(request, 'accounts/dashboard.html', {'my_trips': my_trips})
    else:
        raise PermissionDenied("Only captains can access this dashboard.")

@login_required
def edit_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, captain=request.user)
    if request.method == 'POST':
        form = TripCreationForm(request.POST, request.FILES, instance=trip)  # Include request.FILES for image updates
        if form.is_valid():
            form.save()
            return redirect('captain_dashboard')
    else:
        form = TripCreationForm(instance=trip)
    
    return render(request, 'trips/edit_trip.html', {'form': form, 'trip': trip})
