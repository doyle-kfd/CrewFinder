from django.shortcuts import render
from trips.models import Trip

# Create your views here.
def home(request):
    # Fetch the latest three trips to display on the home page
    trips = Trip.objects.order_by('-date')[:3]
    return render(request, 'pages/home.html', {'trips': trips})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def sailing_opportunities(request):
    # Display all available trips on the Sailing Opportunities page
    trips = Trip.objects.all()
    return render(request, 'pages/sailing_opportunities.html', {'trips': trips})