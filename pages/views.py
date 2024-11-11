from django.shortcuts import render
from django.core.paginator import Paginator
from trips.models import Trip
from crewbooking.models import CrewBooking  # Import the CrewBooking model

# Create your views here.
def home(request):
    trips = Trip.objects.order_by('-date')[:3]  # Fetch the latest three trips

    # Fetch applied trip IDs if the user is logged in
    if request.user.is_authenticated:
        applied_trip_ids = CrewBooking.objects.filter(user=request.user).values_list('trip_id', flat=True)
    else:
        applied_trip_ids = []

    return render(request, 'pages/home.html', {
        'trips': trips,
        'applied_trip_ids': applied_trip_ids,
    })

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def sailing_opportunities(request):
    trips = Trip.objects.all()  # Fetch all trips

    # Fetch applied trip IDs if the user is logged in
    if request.user.is_authenticated:
        applied_trip_ids = CrewBooking.objects.filter(user=request.user).values_list('trip_id', flat=True)
    else:
        applied_trip_ids = []

    return render(request, 'pages/sailing_opportunities.html', {
        'trips': trips,
        'applied_trip_ids': applied_trip_ids,
    })