from django.shortcuts import render
from django.core.paginator import Paginator
from trips.models import Trip
from crewbooking.models import CrewBooking  # Import the CrewBooking model

# Create your views here.
def home(request):
    trips = Trip.objects.order_by('-departure_date')[:3]  # Fetch the latest three trips

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
    trips = Trip.objects.all().order_by('-departure_date')  # Fetch all trips and order by departure date

    # Implement pagination
    paginator = Paginator(trips, 6)  # Show 6 trips per page
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the trips for the current page

    # Fetch applied trip IDs if the user is logged in
    if request.user.is_authenticated:
        applied_trip_ids = CrewBooking.objects.filter(user=request.user).values_list('trip_id', flat=True)
    else:
        applied_trip_ids = []

    return render(request, 'pages/sailing_opportunities.html', {
        'trips': page_obj,  # Pass the paginated trips
        'applied_trip_ids': applied_trip_ids,
    })

def custom_404_view(request, exception=None):
    return render(request, 'pages/404.html', status=404)