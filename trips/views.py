from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied  # Import PermissionDenied
from .models import Trip  # Import the Trip model
from .forms import TripCreationForm

@login_required
def create_trip(request):
    if request.user.role != "captain":
        raise PermissionDenied("Only captains can create trips.")
    
    if request.method == 'POST':
        form = TripCreationForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.captain = request.user
            trip.save()
            return redirect('captain_dashboard')
    else:
        form = TripCreationForm()
    return render(request, 'trips/create_trip.html', {'form': form})

@login_required
def captain_dashboard(request):
    if request.user.role == "captain":
        my_trips = Trip.objects.filter(captain=request.user)
        # Pass captain-specific data to the shared dashboard template
        return render(request, 'accounts/dashboard.html', {'my_trips': my_trips})
    else:
        raise PermissionDenied("Only captains can access this dashboard.")
