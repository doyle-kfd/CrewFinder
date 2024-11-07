from django.shortcuts import render
from django.core.paginator import Paginator
from trips.models import Trip

# Create your views here.
def home(request):
    # Fetch trips created by any captain, limited to 6
    trips = Trip.objects.all().order_by('date')[:6]  # Display the first 6 trips
    return render(request, 'pages/home.html', {'trips': trips})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def sailing_opportunities(request):
    # Retrieve all trips sorted by date
    trips = Trip.objects.all().order_by('date')
    
    # Set up pagination
    paginator = Paginator(trips, 9)  # Show 9 trips per page (3 rows of 3)
    page_number = request.GET.get('page')  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)  # Get the page object

    # Determine if pagination is needed
    show_pagination = paginator.num_pages > 1

    return render(request, 'pages/sailing_opportunities.html', {'page_obj': page_obj, 'show_pagination': show_pagination})