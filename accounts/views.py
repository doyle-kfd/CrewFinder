from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from allauth.account.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .forms import (
    CustomSignupForm,
    ProfileCompletionForm,
    EditUserForm
)
from .models import User
from trips.models import Trip
from crewbooking.models import CrewBooking
from allauth.account.views import SignupView


# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'account/login.html'


# Custom Logout View
class CustomLogoutView(LogoutView):
    next_page = '/'


class CustomPasswordResetView(PasswordResetView):
    template_name = "account/password_reset.html"  # The form for entering an email address
    email_template_name = 'account/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_sent')  # Redirect after submitting the email



# Custom Password Reset Views
class CustomPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html'
    success_url = reverse_lazy('accounts:account_reset_password_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "account/password_reset_sent.html"  # Custom confirmation page


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:account_reset_password_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'


# User Signup View
class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'account/signup.html'
    

    def form_valid(self, form):
        user = form.save(self.request)
        return redirect(reverse_lazy('accounts:registration_pending'))


@login_required
def complete_profile(request):
    if request.user.profile_completed:
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            request.user.profile_completed = True
            request.user.save(update_fields=['profile_completed'])
            return redirect('accounts:dashboard')
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, 'accounts/complete_profile.html', {'form': form})


@login_required
def dashboard(request):
    if request.user.role == User.ADMINISTRATOR:
        return redirect('accounts:admin_dashboard')

    if request.user.role == User.CAPTAIN:
        my_trips = Trip.objects.filter(captain=request.user).select_related('crewbooking_set').order_by('-departure_date')
        return render(request, 'accounts/dashboard.html', {'my_trips': my_trips})

    elif request.user.role == User.CREW:
        applied_trips = CrewBooking.objects.filter(user=request.user).select_related('trip')
        return render(request, 'accounts/dashboard.html', {'applied_trips': applied_trips})

    raise PermissionDenied


@login_required
def admin_dashboard(request):
    if request.user.role != User.ADMINISTRATOR:
        raise PermissionDenied

    users = User.objects.filter(role__in=[User.CAPTAIN, User.CREW]).exclude(is_superuser=True)
    return render(request, 'accounts/admin_dashboard.html', {'users': users})


@login_required
def edit_user(request, user_id):
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

    return render(request, 'accounts/edit_user.html', {'form': form})


@login_required
def crew_profile(request, user_id, trip_id):
    crew_member = get_object_or_404(User, id=user_id)
    crew_booking = get_object_or_404(CrewBooking, user=crew_member, trip_id=trip_id)

    if request.method == 'POST':
        form = CrewBookingStatusForm(request.POST, instance=crew_booking)
        if form.is_valid():
            form.save()
            return redirect('accounts:dashboard')
    else:
        form = CrewBookingStatusForm(instance=crew_booking)

    return render(request, 'accounts/crew_profile.html', {'crew_member': crew_member, 'form': form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('accounts:dashboard')
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, 'accounts/update_profile.html', {'form': form})


def registration_pending(request):
    return render(request, 'accounts/registration_pending.html')


def inactive_account_redirect(request):
    return redirect('accounts:registration_pending')
