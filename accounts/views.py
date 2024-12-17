"""
Account Views
This module defines custom views for managing user accounts,
including authentication, profile management, and administrative functionality.

Dependencies:
- Django's built-in authentication views
- Custom forms and models for handling user-specific features
"""

# Imports
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetDoneView,
    PasswordResetCompleteView, PasswordResetView, PasswordResetConfirmView
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from .forms import CustomSignupForm, ProfileCompletionForm, EditUserForm
from .models import User
from trips.models import Trip
from crewbooking.models import CrewBooking
from allauth.account.views import SignupView
from .forms import CrewBookingStatusForm


# Password Reset Views
class CustomPasswordResetView(PasswordResetView):
    """
    Handles the password reset initiation process.
    Displays a form for users to enter their email, then sends a
    password reset email containing a token and user ID.
    """
    email_template_name = "account/password_reset_email.html"
    template_name = "account/password_reset.html"
    success_url = reverse_lazy("accounts:password_reset_done")


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Handles the password reset confirmation process.
    Allows users to set a new password using a valid reset link.
    """
    template_name = "account/password_reset_confirm.html"

    def get_success_url(self):
        """
        Redirects to the password reset completion page on success.
        """
        return reverse_lazy("accounts:account_reset_password_complete")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    """
    Displays a success message after a password reset email has been sent.
    """
    template_name = "account/password_reset_done.html"


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """
    Displays a success message after the password has been successfully reset.
    """
    template_name = "account/password_reset_complete.html"


# Authentication Views
class CustomLoginView(LoginView):
    """
    Handles user login and displays a login form.
    """
    template_name = "account/login.html"


class CustomLogoutView(LogoutView):
    """
    Logs the user out and redirects to the homepage.
    """
    next_page = "/"


class CustomSignupView(SignupView):
    """
    Custom Signup View to handle user registration logic.
    """
    form_class = CustomSignupForm
    template_name = "account/signup.html"

    def form_valid(self, form):
        """
        Overridden form_valid method to ensure `request` is passed to save().
        """
        user = form.save(self.request)  # Pass the request to save method
        return redirect(reverse_lazy("accounts:registration_pending"))


# Profile Management Views
@login_required
def complete_profile(request):
    """
    Allows users to complete their profile after registration.
    Redirects to the dashboard if the profile is already completed.
    """
    if request.user.profile_completed:
        return redirect("accounts:dashboard")

    if request.method == "POST":
        form = ProfileCompletionForm(
            request.POST, request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
            request.user.profile_completed = True
            request.user.save(update_fields=["profile_completed"])
            return redirect("accounts:dashboard")
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, "accounts/complete_profile.html", {"form": form})


@login_required
def update_profile(request):
    """
    Allows users to update their profile information.
    Displays a pre-populated form and saves valid updates.
    """
    if request.method == "POST":
        form = ProfileCompletionForm(
            request.POST, request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("accounts:dashboard")
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, "accounts/update_profile.html", {"form": form})


# Dashboard Views
@login_required
def dashboard(request):
    """
    Displays a role-specific dashboard for the logged-in user:
    - Administrators are redirected to the admin dashboard.
    - Captains see a list of their created trips.
    - Crew members see the trips they have applied for.
    """
    if request.user.role == User.ADMINISTRATOR:
        return redirect("accounts:admin_dashboard")

    if request.user.role == User.CAPTAIN:
        my_trips = Trip.objects.filter(
            captain=request.user
        ).order_by("-departure_date")
        return render(request, "accounts/dashboard.html",
                      {"my_trips": my_trips})

    elif request.user.role == User.CREW:
        applied_trips = CrewBooking.objects.filter(
            user=request.user
        ).select_related("trip").order_by("-trip__departure_date")
        return render(
            request, "accounts/dashboard.html",
                     {"applied_trips": applied_trips}
        )

    raise PermissionDenied


@login_required
def admin_dashboard(request):
    """
    Displays the admin dashboard.
    Lists all users with roles 'Captain' and 'Crew', excluding superusers.
    """
    if request.user.role != User.ADMINISTRATOR:
        raise PermissionDenied

    users = User.objects.filter(
        role__in=[User.CAPTAIN, User.CREW]
    ).exclude(is_superuser=True)
    return render(request, "accounts/admin_dashboard.html", {"users": users})


@login_required
def edit_user(request, user_id):
    """
    Allows administrators to edit user details.
    """
    if request.user.role != User.ADMINISTRATOR:
        raise PermissionDenied

    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("accounts:admin_dashboard")
    else:
        form = EditUserForm(instance=user)

    return render(request, "accounts/edit_user.html", {"form": form})



@login_required
def crew_profile(request, user_id, trip_id):
    """
    Displays a crew member's profile for a specific trip.
    Captains can update the crew booking status for the trip.
    """
    crew_member = get_object_or_404(User, id=user_id)
    crew_booking = get_object_or_404(CrewBooking, user=crew_member,
                                     trip_id=trip_id)

    if request.method == "POST":

        form = CrewBookingStatusForm(request.POST, instance=crew_booking)
        if form.is_valid():
            form.save()
            return redirect("accounts:dashboard")
    else:
        form = CrewBookingStatusForm(instance=crew_booking)

    return render(
        request,
        "accounts/crew_profile.html",
        {"crew_member": crew_member, "form": form},
    )


# Registration and Inactive Redirect Views
def registration_pending(request):
    """
    Displays a message indicating that the user's registration is
    pending approval.
    """
    return render(request, "accounts/registration_pending.html")


def inactive_account_redirect(request):
    """
    Redirects inactive accounts to the registration pending page.
    """
    return redirect("accounts:registration_pending")
