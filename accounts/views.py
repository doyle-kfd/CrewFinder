"""
Account Views
This module defines custom views for managing user accounts,
including authentication,
profile management, and administrative functionality.

Dependencies:
- Django's built-in authentication views
- allauth account views for user signup and password reset
- Custom forms and models for handling user-specific features
"""

# Imports
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordResetView,
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from allauth.account.views import SignupView

from .forms import CustomSignupForm, ProfileCompletionForm, EditUserForm
from .models import User
from trips.models import Trip
from crewbooking.models import CrewBooking


# Custom Authentication and Password Views
class CustomLoginView(LoginView):
    """
    Custom login view that uses a custom template for the login page.
    """
    template_name = 'account/login.html'


class CustomLogoutView(LogoutView):
    """
    Custom logout view that redirects users to the homepage after logout.
    """
    next_page = '/'


class CustomPasswordResetView(PasswordResetView):
    """
    Custom password reset view with customized email template and
    success redirect.
    """
    template_name = "account/password_reset.html"
    email_template_name = 'account/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_sent')


class CustomPasswordChangeView(PasswordChangeView):
    """
    Custom password change view with success redirect to a confirmation page.
    """

    success_url = reverse_lazy('accounts:password_change_done')

    def form_valid(self, form):
        """
        Handle valid password change form by saving the password and
        retaining the session.
        """
        form.save()
        return super().form_valid(form)


class CustomPasswordResetDoneView(PasswordResetDoneView):
    """
    View for displaying a confirmation page after requesting a password reset.
    """
    template_name = "account/password_reset_sent.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """
    View for confirming password reset and setting a new password.
    """
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:account_reset_password_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """
    View for displaying a confirmation page after completing a password reset.
    """
    template_name = 'account/password_reset_complete.html'


# Custom User Management Views
class CustomSignupView(SignupView):
    """
    Custom signup view for user registration using a custom form.
    """
    form_class = CustomSignupForm
    template_name = 'account/signup.html'

    def form_valid(self, form):
        """
        Handle valid signup form by saving the user and redirecting to a
        pending page.
        """
        user = form.save(self.request)
        return redirect(reverse_lazy('accounts:registration_pending'))


@login_required
def complete_profile(request):
    """
    View for users to complete their profile after registration.
    """
    if request.user.profile_completed:
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST,
                                     request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            request.user.profile_completed = True
            request.user.save(update_fields=['profile_completed'])
            return redirect('accounts:dashboard')
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, 'accounts/complete_profile.html',
                  {'form': form})


@login_required
def dashboard(request):
    """
    View to render the user dashboard based on their role:
    - Captains see their trips and applicants.
    - Crew members see trips they have applied for.
    - Administrators are redirected to the admin dashboard.
    """
    if request.user.role == User.ADMINISTRATOR:
        return redirect('accounts:admin_dashboard')

    if request.user.role == User.CAPTAIN:
        my_trips = Trip.objects.filter(captain=request.user)\
            .prefetch_related('crewbooking_set__user')\
            .order_by('-departure_date')
        return render(request, 'accounts/dashboard.html',
                      {'my_trips': my_trips})

    elif request.user.role == User.CREW:
        applied_trips = CrewBooking.objects.filter(user=request.user)\
            .select_related('trip')\
            .order_by('-trip__departure_date')
        return render(request, 'accounts/dashboard.html',
                      {'applied_trips': applied_trips})

    raise PermissionDenied


@login_required
def admin_dashboard(request):
    """
    View for administrators to manage user accounts for captains
    and crew members.
    """
    if request.user.role != User.ADMINISTRATOR:
        raise PermissionDenied

    users = (User.objects.filter
             (role__in=[User.CAPTAIN, User.CREW]).exclude(is_superuser=True))
    return render(request, 'accounts/admin_dashboard.html',
                  {'users': users})


@login_required
def edit_user(request, user_id):
    """
    View for administrators to edit user details.
    """
    if request.user.role != User.ADMINISTRATOR:
        raise PermissionDenied

    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:admin_dashboard')
    else:
        form = EditUserForm(instance=user)

    return render(request, 'accounts/edit_user.html',
                  {'form': form})


@login_required
def crew_profile(request, user_id, trip_id):
    """
    View for captains to view and manage a crew member's application
    for a trip.
    """
    from .forms import CrewBookingStatusForm

    crew_member = get_object_or_404(User, id=user_id)
    crew_booking = get_object_or_404(CrewBooking, user=crew_member,
                                     trip_id=trip_id)

    if request.method == 'POST':
        form = CrewBookingStatusForm(request.POST, instance=crew_booking)
        if form.is_valid():
            form.save()
            return redirect('accounts:dashboard')
    else:
        form = CrewBookingStatusForm(instance=crew_booking)

    return render(request, 'accounts/crew_profile.html',
                  {'crew_member': crew_member, 'form': form})


@login_required
def update_profile(request):
    """
    View for users to update their profile details.
    """
    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, request.FILES,
                                     instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile"
                                      " has been updated.")
            return redirect('accounts:dashboard')
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, 'accounts/update_profile.html',
                  {'form': form})


def registration_pending(request):
    """
    View for displaying a pending registration page for
     users awaiting approval.
    """
    return render(request, 'accounts/registration_pending.html')


def inactive_account_redirect(request):
    """
    Redirect users with inactive accounts to the registration pending page.
    """
    return redirect('accounts:registration_pending')
