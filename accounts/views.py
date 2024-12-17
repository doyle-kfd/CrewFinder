"""
Account Views
This module defines custom views for managing user accounts,
including authentication, profile management, and administrative functionality.

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
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordResetView,
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from allauth.account.views import SignupView, PasswordResetFromKeyView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordResetConfirmView
from django.utils.http import urlencode
import logging

from .forms import CustomSignupForm, ProfileCompletionForm, EditUserForm
from .models import User
from trips.models import Trip
from crewbooking.models import CrewBooking
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

logger = logging.getLogger('accounts')


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "account/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:account_reset_password_complete")
    print("IM USING THE CUSTOM VIEW")

    def dispatch(self, request, *args, **kwargs):
        # Debug for clarity
        uidb64 = kwargs.get("uidb64")
        token = kwargs.get("token")
        print(f"Password reset link accessed with UIDB64={uidb64}, Token={token}")
        return super().dispatch(request, *args, **kwargs)


class CustomPasswordResetView(PasswordResetView):
    """
    Custom Password Reset View to generate and log uidb64 and token before sending the email.
    """
    email_template_name = "account/password_reset_email.html"
    template_name = "account/password_reset.html"
    success_url = reverse_lazy("accounts:password_reset_done")
    token_generator = default_token_generator

    def form_valid(self, form):
        user_email = form.cleaned_data.get("email")
        logger.debug(f"Password reset initiated for: {user_email}")

        for user in form.get_users(user_email):
            if user is None:
                logger.error("No user found for the given email.")
                continue

            # Generate UID and Token
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = self.token_generator.make_token(user)

            # Log or Print UIDB64 and Token
            print(f"Generated UIDB64: {uidb64}")  # Print in the console
            print(f"Generated Token: {token}")   # Print in the console
            logger.debug(f"Generated UIDB64: {uidb64}, Token: {token}")  # Log the values


            # Set production domain explicitly
            production_domain = 'crew-finder-410f29f97c51.herokuapp.com'

            # Email Context
            context = {
                'uid': uidb64,
                'token': token,
                'protocol': self.request.scheme,
                'domain': production_domain,  # Explicitly set production domain
                #'domain': self.request.get_host(),
            }

            # Render the email
            subject = "Password Reset Request"
            email_message = render_to_string(self.email_template_name, context)

            # Log rendered email for debugging
            print(f"Email Subject: {subject}")
            print(f"Rendered Email: {email_message}")
            logger.debug(f"Rendered Email Content: {email_message}")

            # Send the email
            # send_mail(subject, email_message, None, [user_email])

        return super().form_valid(form)


"""
class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):

    def dispatch(self, request, *args, **kwargs):
        uidb36 = kwargs.get("uidb36")
        key = kwargs.get("key")
        logger.debug(f"Reset URL received: UIDB36={uidb36}, Key={key}")
        return super().dispatch(request, *args, **kwargs)

"""

# Password Reset Done and Complete Views
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "account/password_reset_done.html"

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "account/password_reset_complete.html"

# Custom Login and Logout Views
class CustomLoginView(LoginView):
    template_name = "account/login.html"

class CustomLogoutView(LogoutView):
    next_page = "/"

# Custom Signup View
class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = "account/signup.html"

    def form_valid(self, form):
        user = form.save(self.request)
        return redirect(reverse_lazy("accounts:registration_pending"))

# Profile Completion and Update Views
@login_required
def complete_profile(request):
    if request.user.profile_completed:
        return redirect("accounts:dashboard")

    if request.method == "POST":
        form = ProfileCompletionForm(request.POST, request.FILES, instance=request.user)
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
    if request.method == "POST":
        form = ProfileCompletionForm(request.POST, request.FILES, instance=request.user)
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
    if request.user.role == User.ADMINISTRATOR:
        return redirect("accounts:admin_dashboard")

    if request.user.role == User.CAPTAIN:
        my_trips = Trip.objects.filter(captain=request.user).order_by("-departure_date")
        return render(request, "accounts/dashboard.html", {"my_trips": my_trips})

    elif request.user.role == User.CREW:
        applied_trips = CrewBooking.objects.filter(user=request.user).select_related("trip").order_by("-trip__departure_date")
        return render(request, "accounts/dashboard.html", {"applied_trips": applied_trips})

    raise PermissionDenied

@login_required
def admin_dashboard(request):
    if request.user.role != User.ADMINISTRATOR:
        raise PermissionDenied

    users = User.objects.filter(role__in=[User.CAPTAIN, User.CREW]).exclude(is_superuser=True)
    return render(request, "accounts/admin_dashboard.html", {"users": users})

@login_required
def edit_user(request, user_id):
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
    crew_member = get_object_or_404(User, id=user_id)
    crew_booking = get_object_or_404(CrewBooking, user=crew_member, trip_id=trip_id)

    if request.method == "POST":
        from .forms import CrewBookingStatusForm
        form = CrewBookingStatusForm(request.POST, instance=crew_booking)
        if form.is_valid():
            form.save()
            return redirect("accounts:dashboard")
    else:
        form = CrewBookingStatusForm(instance=crew_booking)

    return render(request, "accounts/crew_profile.html", {"crew_member": crew_member, "form": form})

# Registration Pending and Inactive Redirect Views
def registration_pending(request):
    return render(request, "accounts/registration_pending.html")

def inactive_account_redirect(request):
    return redirect("accounts:registration_pending")
