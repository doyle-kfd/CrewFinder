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
from django.contrib.sites.models import Site
from django.conf import settings
from django.urls import reverse

from .forms import CustomSignupForm, ProfileCompletionForm, EditUserForm
from .models import User
from trips.models import Trip
from crewbooking.models import CrewBooking
from django.contrib.auth.forms import PasswordResetForm

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect

def custom_password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            users = User.objects.filter(email=email)
            for user in users:
                context = {
                    "email": email,
                    "domain": request.get_host(),
                    "site_name": "CrewFinder",
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": default_token_generator.make_token(user),
                    "protocol": "https" if request.is_secure() else "http",
                }
                subject = "Reset Your Password"
                email_template_name = "account/password_reset_email.html"
                email_content = render_to_string(email_template_name, context)
                send_mail(subject, email_content, settings.DEFAULT_FROM_EMAIL, [email])
            return redirect("accounts:password_reset_done")
    else:
        form = PasswordResetForm()

    return render(request, "account/password_reset_form.html", {"form": form})


from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render, redirect

from django.contrib.auth.tokens import default_token_generator
import logging


logger = logging.getLogger(__name__)

class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        logger.info("Password reset form submitted successfully.")
        for user in form.get_users():
            token = default_token_generator.make_token(user)
            if token:
                logger.debug(f"Generated token for user {user.id}: {token}")
            else:
                logger.error(f"Failed to generate token for user {user.id}")
        return super().form_valid(form)

from allauth.account.views import PasswordResetFromKeyView

class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.debug(f"Reset URL context: uidb36={context.get('uidb36')}, key={context.get('key')}")
        return context

def custom_password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect("accounts:password_reset_complete")
        else:
            form = SetPasswordForm(user)
        return render(request, "account/password_reset_confirm.html", {"form": form})
    else:
        return render(request, "account/password_reset_invalid.html")

def custom_password_reset_done(request):
    return render(request, "account/password_reset_done.html")


def custom_password_reset_complete(request):
    return render(request, "account/password_reset_complete.html")


from django.http import HttpResponse

def debug_view(request, uidb36, key):
    return HttpResponse(f"UID: {uidb36}, Key: {key}")

class DebugPasswordResetForm(PasswordResetForm):
    def save(self, domain_override=None,
             subject_template_name=None,
             email_template_name=None,
             use_https=False,
             token_generator=None,
             from_email=None,
             request=None,
             html_email_template_name=None,
             extra_email_context=None):
        print("DebugPasswordResetForm save called")
        print("Domain Override:", domain_override)
        print("Subject Template Name:", subject_template_name)
        print("Email Template Name:", email_template_name)
        print("Request:", request)
        print("Extra Email Context:", extra_email_context)
        return super().save(
            domain_override=domain_override,
            subject_template_name=subject_template_name,
            email_template_name=email_template_name,
            use_https=use_https,
            token_generator=token_generator,
            from_email=from_email,
            request=request,
            html_email_template_name=html_email_template_name,
            extra_email_context=extra_email_context,
        )

    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None):
        print("DebugPasswordResetForm send_mail called. UID:", context.get("uid"), "Token:", context.get("token"))
        print("Full Context:", context)
        super().send_mail(subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name)


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

"""
class CustomPasswordResetView(PasswordResetView):
    template_name = "account/password_reset.html"
    email_template_name = "account/password_reset_email.html"
    success_url = reverse_lazy('accounts:password_reset_sent')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("CustomPasswordResetView initialized")

    def get_email_context(self, *args, **kwargs):
        context = super().get_email_context(*args, **kwargs)
        # Debugging: Print UID and Token
        print("UID (Base36):", context.get("uid"))  # Should print the base36-encoded user ID
        print("Token:", context.get("token"))  # Should print the password reset token
        try:
            current_site = Site.objects.get(id=settings.SITE_ID)
            context['domain'] = current_site.domain
        except Site.DoesNotExist:
            context['domain'] = 'crew-finder-410f29f97c51.herokuapp.com'
        context['protocol'] = 'https'
        return context

    def form_valid(self, form):
        # Debugging: Confirm form submission
        print("Password reset form is valid. Sending email...")
        response = super().form_valid(form)
        return response
"""

class CustomPasswordResetView(PasswordResetView):
    form_class = DebugPasswordResetForm
    template_name = "account/password_reset.html"
    email_template_name = "account/password_reset_email.html"
    success_url = reverse_lazy('accounts:password_reset_sent')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domain'] = self.request.get_host()  # Set the domain dynamically
        return context


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
