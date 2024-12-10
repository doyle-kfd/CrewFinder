"""
Views for the pages app in the CrewFinder project.

This module defines the view functions for rendering static pages,
handling contact form submissions,
displaying sailing opportunities with pagination,
and managing custom error pages.

Functions:
- `home`: Displays the home page with the latest trips and
          user-specific applied trip IDs.
- `about`: Renders the about page with static content.
- `contact`: Handles contact form submissions and sends emails.
- `sailing_opportunities`: Lists all trips with pagination and user-specific
                           applied trip IDs.
- `custom_404_view`, `custom_403_view`, `custom_400_view`,
  `custom_500_view`: Custom error handlers.
- `test_400_view`, `test_403_view`,
  `test_500_view`: Test views for error pages.
- `manual_500_view`: Manually renders the 500 error page for testing.

"""

from django.shortcuts import render
from django.core.paginator import Paginator
from trips.models import Trip
# Import the CrewBooking model
from crewbooking.models import CrewBooking
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.exceptions import (PermissionDenied, BadRequest,
                                    SuspiciousOperation)
from django.http import HttpResponseBadRequest
import sys
from django.urls import reverse, NoReverseMatch


def home(request):
    """
    Displays the home page with the latest trips.

    Fetches the latest three trips and, if the user is authenticated,
    retrieves the IDs of trips they have applied for.
    """
    trips = Trip.objects.order_by('-departure_date')[:3]
    applied_trip_ids = (
        CrewBooking.objects.filter(user=request.user).values_list('trip_id', flat=True)
        if request.user.is_authenticated else []
    )

    # Attempt to resolve the complete_profile URL
    try:
        complete_profile_url = reverse('accounts:complete_profile')
    except NoReverseMatch as e:
        complete_profile_url = None
        print(f"Error resolving 'complete_profile': {e}")

    return render(request, 'pages/home.html', {
        'trips': trips,
        'applied_trip_ids': applied_trip_ids,
        'complete_profile_url': complete_profile_url,  # Pass the URL to the template
    })


def about(request):
    """
    Renders the about page with static content.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered about page.
    """
    return render(request, 'pages/about.html')


def contact(request):
    """
    Handles contact form submissions and sends an email.

    If the request method is POST, retrieves form data (name, email, message),
    logs it to the console, and sends an email to the specified recipient.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered contact page with success or error messages.
    """
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Name: {name}, Email: {email},  Message: {message}",
              file=sys.stdout)

        subject = f"Message from {name} via CrewFinder Contact Form"
        email_message = f"Name: {name}\nEmail:  {email}\n\nMessage:\
        n{message}\n"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        try:
            send_mail(subject, email_message, from_email,  recipient_list,
                      fail_silently=False)
            messages.success(request,  "Your message has been sent "
                                       "successfully!")
        except Exception as e:
            messages.error(request,  f"An error occurred while sending the "
                                     f"email: {e}")

    return render(request, "pages/contact.html")


def sailing_opportunities(request):
    """
    Displays the Sailing Opportunities page with trip listings and pagination.

    Fetches all trips, applies pagination, and retrieves
    applied trip IDs if the user is authenticated.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered Sailing Opportunities page with:
      - `trips`: The paginated trips for the current page.
      - `applied_trip_ids`: List of trip IDs the user has applied for.
    """
    trips = Trip.objects.all().order_by('-departure_date')
    paginator = Paginator(trips, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    applied_trip_ids = (
        CrewBooking.objects.filter(user=request.user). values_list(
            'trip_id', flat=True)
        if request.user.is_authenticated else []
    )
    return render(request, 'pages/sailing_opportunities.html',
                  {'trips': page_obj,
                   'applied_trip_ids': applied_trip_ids,
                   })


def custom_404_view(request, exception=None):
    """
    Custom handler for 404 errors (Page Not Found).

    Parameters:
    - request: The HTTP request object.
    - exception: The exception that triggered the error (optional).

    Returns:
    - Rendered 404 error page with status code 404.
    """
    return render(request, 'pages/404.html', status=404)


def custom_403_view(request, exception=None):
    """
    Custom handler for 403 errors (Permission Denied).

    Parameters:
    - request: The HTTP request object.
    - exception: The exception that triggered the error (optional).

    Returns:
    - Rendered 403 error page with status code 403.
    """
    return render(request, 'pages/403.html', status=403)


def custom_400_view(request, exception=None):
    """
    Custom handler for 400 errors (Bad Request).

    Parameters:
    - request: The HTTP request object.
    - exception: The exception that triggered the error (optional).

    Returns:
    - Rendered 400 error page with status code 400.
    """
    return render(request, 'pages/400.html', status=400)


def custom_500_view(request, exception=None):
    """
    Custom handler for 500 errors (Internal Server Error).

    Parameters:
    - request: The HTTP request object.
    - exception: The exception that triggered the error (optional).

    Returns:
    - Rendered 500 error page with status code 500.
    """
    return render(request, 'pages/500.html', status=500)


# Test Views for Error Pages
def test_400_view(request):
    """
    Simulates a 400 Bad Request error for testing purposes.

    Parameters:
    - request: The HTTP request object.

    Raises:
    - BadRequest: Custom error for testing.
    """
    raise BadRequest("This is a test 400 error.")


def test_403_view(request):
    """
    Simulates a 403 Permission Denied error for testing purposes.

    Parameters:
    - request: The HTTP request object.

    Raises:
    - PermissionDenied: Custom error for testing.
    """
    raise PermissionDenied("This is a test 403 error.")


def test_500_view(request):
    """
    Simulates a 500 Internal Server Error for testing purposes.

    Parameters:
    - request: The HTTP request object.

    Raises:
    - Exception: Custom error for testing.
    """
    raise Exception("This is a test 500 error.")


def manual_500_view(request):
    """
    Renders a manually created 500 error page for testing purposes.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered 500 error page with status code 500.
    """
    return render(request, 'pages/500.html', status=500)
