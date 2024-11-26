from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django import forms
from django.db.models import Count, Prefetch
from .forms import ProfileCompletionForm, EditUserForm
from .models import User
from trips.models import Trip
from crewbooking.models import CrewBooking
from allauth.account.views import SignupView


@login_required
def complete_profile(request):
    """
    Allows a user to complete their profile if it has not been completed yet.
    Redirects the user to the dashboard if the profile is already complete.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response for completing the profile or
        a redirect to the dashboard.
    """
    if request.user.profile_completed:
        return redirect('dashboard')

    if request.method == 'POST':
        form = ProfileCompletionForm(
            request.POST, request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
            request.user.profile_completed = True
            request.user.save(update_fields=['profile_completed'])
            return redirect('dashboard')
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, 'accounts/complete_profile.html', {'form': form})


@login_required
def dashboard(request):
    """
    Renders the user dashboard based on their role. Redirects administrators
    to the admin dashboard and displays trips for captains or applications
    for crew members.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered dashboard for the respective user role.
    """
    if request.user.role == User.ADMINISTRATOR:
        return redirect('admin_dashboard')

    if request.user.role == 'captain':
        my_trips = Trip.objects.filter(captain=request.user).prefetch_related(
            Prefetch(
                'crewbooking_set',
                queryset=CrewBooking.objects.select_related('user')
                .order_by('status'),
                to_attr='applicants'
            )
        ).annotate(applicant_count=Count('crewbooking')).order_by(
            '-departure_date'
        )

        return render(request, 'accounts/dashboard.html',
                      {'my_trips': my_trips})

    elif request.user.role == 'crew':
        applied_trips = CrewBooking.objects.filter(
            user=request.user
        ).select_related('trip')

        return render(request, 'accounts/dashboard.html', {
            'applied_trips': applied_trips,
        })

    raise PermissionDenied("You are not authorized to view this page.")


def registration_pending(request):
    """
    Renders the registration pending page for users awaiting approval.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered registration pending page.
    """
    return render(request, 'accounts/registration_pending.html')


class CustomLoginView(LoginView):
    """
    Custom login view to handle user authentication and redirect based on
    user role and profile completion status.

    Attributes:
        template_name (str): Path to the login template.
    """
    template_name = 'account/login.html'

    def form_valid(self, form):
        """
        Redirects the user to the appropriate page after successful login.

        Args:
            form (AuthenticationForm): The validated authentication form.

        Returns:
            HttpResponse: The redirection to the appropriate dashboard or page.
        """
        user = form.get_user()
        next_url = self.request.GET.get('next', None)

        if user.is_authenticated:
            if user.role == 'administrator':
                return redirect('admin_dashboard')
            elif not user.profile_completed:
                return redirect('complete_profile')
            if next_url:
                return redirect(next_url)

            return redirect('dashboard')

        return super().form_valid(form)


class CustomSignupView(SignupView):
    """
    Custom signup view to redirect new users to the registration pending page.
    """

    def form_valid(self, form):
        """
        Saves the user and redirects to the registration pending page.

        Args:
            form (SignupForm): The validated signup form.

        Returns:
            HttpResponse: The redirection to the registration pending page.
        """
        user = form.save(self.request)
        return redirect(reverse('registration_pending'))


@login_required
def admin_dashboard(request):
    """
    Renders the admin dashboard, showing users with Captain and Crew roles.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered admin dashboard.
    """
    if request.user.role == User.ADMINISTRATOR:
        users = User.objects.filter(
            role__in=[User.CAPTAIN, User.CREW],
            is_superuser=False
        ).order_by('is_active')

        return render(request, 'accounts/admin_dashboard.html',
                      {'users': users})
    else:
        return redirect('dashboard')


class CustomLogoutView(LogoutView):
    """
    Custom logout view that redirects users to the home page with a message.

    Attributes:
        next_page (str): Path to redirect after logout.
    """
    next_page = '/'

    def dispatch(self, request, *args, **kwargs):
        """
        Handles the logout process and adds a success message.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: The redirection to the next page after logout.
        """
        messages.success(request, "You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)


@login_required
def update_profile(request):
    """
    Allows a user to update their profile, including uploading files.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered update profile page or a redirect
        to the dashboard after updating.
    """
    if request.method == 'POST':
        form = ProfileCompletionForm(
            request.POST, request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('dashboard')
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, 'accounts/update_profile.html', {'form': form})


class CrewBookingStatusForm(forms.ModelForm):
    """
    Form for updating the status of a crew booking.

    Attributes:
        Meta (class): Metadata for the form, specifying the model and fields.
    """
    class Meta:
        model = CrewBooking
        fields = ['status']


@login_required
def crew_profile(request, user_id, trip_id):
    """
    Displays and updates a crew member's profile for a specific trip.

    Args:
        request (HttpRequest): The HTTP request object.
        user_id (int): The ID of the crew member.
        trip_id (int): The ID of the trip.

    Returns:
        HttpResponse: The rendered crew profile page.
    """
    crew_member = get_object_or_404(User, id=user_id)
    crew_booking = get_object_or_404(CrewBooking, user=crew_member,
                                     trip_id=trip_id)

    if request.method == 'POST':
        form = CrewBookingStatusForm(request.POST, instance=crew_booking)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CrewBookingStatusForm(instance=crew_booking)

    return render(request, 'accounts/crew_profile.html', {
        'crew_member': crew_member,
        'form': form
    })


@login_required
def edit_user(request, user_id):
    """
    Allows an administrator to edit a user's details.

    Args:
        request (HttpRequest): The HTTP request object.
        user_id (int): The ID of the user to be edited.

    Returns:
        HttpResponse: The rendered edit user page or a redirect
        to the admin dashboard after saving changes.
    """
    if request.user.role != 'administrator':
        return redirect('dashboard')

    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = EditUserForm(instance=user)

    return render(request, 'accounts/edit_user.html', {
        'form': form,
        'user_obj': user
    })
