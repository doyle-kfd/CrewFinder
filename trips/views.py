from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TripForm
from .models import Trip

@login_required
def create_trip(request):
    # Restrict access to Captains
    if request.user.role != 'Captain':
        return redirect('home')

    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.captain = request.user  # Set the captain to the current user
            trip.save()
            return redirect('my_trips')
    else:
        form = TripForm()

    return render(request, 'trips/create_trip.html', {'form': form})

@login_required
def my_trips(request):
    if request.user.role != 'Captain':
        return redirect('home')  # Only Captains can view this page

    trips = Trip.objects.filter(captain=request.user)  # Get trips created by this Captain
    return render(request, 'trips/my_trips.html', {'trips': trips})