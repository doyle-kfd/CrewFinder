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
        CrewBooking.objects.filter(user=request.user).values_list(
            'trip_id', flat=True)
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
        # Pass the URL to the template
        'complete_profile_url': complete_profile_url,
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
    Handles the contact form submissions and sends tailored emails
    to both the admin and the user.

    This view processes POST requests containing the contact form data
    (name, email, and message).

    It performs the following actions:

    1. Logs the submitted form data to the console for debugging purposes.
    2. Sends a detailed email to the site admin, notifying them of
       the submission,
       including the user's name, email, and message content.
    3. Sends a confirmation email to the user, acknowledging receipt
       of their message
       and including a copy of the submitted message.
    4. Displays success or error messages on the contact page,
       depending on the outcome
       of the email-sending process.

    Parameters:
    - request (HttpRequest): The HTTP request object containing form data.

    Returns:
    - HttpResponse: Renders the 'contact.html' template with success or
      error messages.

    Notes:
    - Admin email address is dynamically retrieved from the `EMAIL_HOST_USER`
      setting.
    - User's email address is taken from the form data (`email` field).
    - Uses Django's messages framework to communicate success or failure
      to the user.
    - Sends emails using the configured email backend (defined in
      `settings.py`).
    """
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Log form data to the console
        print(f"Name: {name}, Email: {email}, Message: {message}")

        # Email details for the admin
        subject_to_admin = "New Contact Form Submission via CrewFinder"
        message_to_admin = (
            f"Hello Admin,\n\n"
            "You have received a new message via the CrewFinder"
            " contact form. Below are the details:\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            "Message:\n"
            f"{message}\n\n"
            "Please follow up with the user as needed.\n\n"
            "Best regards,\n"
            "The CrewFinder System"
        )

        # Email details for the user
        subject_to_user = "Thank you for contacting CrewFinder"
        message_to_user = (
            f"Hi {name},\n\n"
            "Thank you for reaching out to CrewFinder! Your"
            " message has been received, and our team will get back"
            " to you shortly.\n\n"
            f"Here’s a copy of your message:\n\n{message}\n\n"
            "Best regards,\n"
            "The CrewFinder Team"
        )

        from_email = settings.EMAIL_HOST_USER

        try:
            # Send email to the admin
            send_mail(
                subject_to_admin,
                message_to_admin,
                from_email,
                [from_email],  # Admin email
                fail_silently=False,
            )
            # Send email to the user
            send_mail(
                subject_to_user,
                message_to_user,
                from_email,
                [email],  # User email
                fail_silently=False,
            )
            messages.success(request, "Your message"
                                      " has been sent successfully!")
        except Exception as e:
            print(f"Error while sending email: {e}")
            messages.error(request, "An error occurred"
                                    " while sending your message."
                                    " Please try again later.")

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
