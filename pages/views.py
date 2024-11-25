from django.shortcuts import render
from django.core.paginator import Paginator
from trips.models import Trip
from crewbooking.models import CrewBooking  # Import the CrewBooking model
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.exceptions import PermissionDenied  # For 403 testing
from django.http import HttpResponseBadRequest
from django.core.exceptions import SuspiciousOperation
from django.core.exceptions import BadRequest
import sys

# Existing views

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
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Name: {name}, Email: {email}, Message: {message}", file=sys.stdout)  # Force print to console

        # Compose the email
        subject = f"Message from {name} via CrewFinder Contact Form"
        email_message = (
            f"Name: {name}\n"
            f"Email: {email}\n\n"
            f"Message:\n{message}\n"
        )
        from_email = settings.EMAIL_HOST_USER  # Your email from settings
        recipient_list = [email]  # Email entered in the form

        try:
            # Send the email
            send_mail(subject, email_message, from_email, recipient_list, fail_silently=False)
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred while sending the email: {e}")

    return render(request, "pages/contact.html")

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

def custom_403_view(request, exception=None):
    return render(request, 'pages/403.html', status=403)

def custom_400_view(request, exception=None):
    return render(request, 'pages/400.html', status=400)

def custom_500_view(request, exception=None):
    return render(request, 'pages/500.html', status=500)

# Test Views for Error Pages
def test_400_view(request):
    raise BadRequest("This is a test 400 error.")

def test_403_view(request):
    raise PermissionDenied("This is a test 403 error.")

def test_500_view(request):
    raise Exception("This is a test 500 error.")

def manual_500_view(request):
    return render(request, 'pages/500.html', status=500)