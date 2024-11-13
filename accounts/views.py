from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ProfileCompletionForm
from .models import User
from allauth.account.views import SignupView
from trips.models import Trip  # Import the Trip model to access trips
from crewbooking.models import CrewBooking  # Import the CrewBooking model
from django import forms  # Import forms module

@login_required
def complete_profile(request):
    if request.user.profile_completed:
        return redirect('dashboard')  # Redirect if profile is already complete

    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, request.FILES, instance=request.user)  # Handle file uploads
        if form.is_valid():
            form.save()  # Save form data
            request.user.profile_completed = True
            request.user.save(update_fields=['profile_completed'])  # Mark profile as complete
            return redirect('dashboard')
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, 'accounts/complete_profile.html', {'form': form})

@login_required
def dashboard(request):
    # Check if the user is an admin and redirect them accordingly
    if request.user.role == User.ADMINISTRATOR:
        return redirect('admin_dashboard')  # Redirect admin to the admin dashboard

    # For captains, show their created trips and applicants
    if request.user.role == 'captain':
        my_trips = Trip.objects.filter(captain=request.user).order_by('-departure_date')  # Get the trips created by the captain
        applied_crews = CrewBooking.objects.filter(trip__captain=request.user)  # Get applicants for those trips
        return render(request, 'accounts/dashboard.html', {'my_trips': my_trips, 'applied_crews': applied_crews})

    # For crew members, show the trips they have applied for with status
    elif request.user.role == 'crew':
        applied_trips = CrewBooking.objects.filter(user=request.user).select_related('trip')  # Get trips and status for each application

        return render(request, 'accounts/dashboard.html', {
            'applied_trips': applied_trips,  # Pass CrewBooking objects with trip and status details
        })

    else:
        # If user role is unknown or invalid, raise permission denied
        raise PermissionDenied("You are not authorized to view this page.")



# Registration pending view
def registration_pending(request):
    return render(request, 'accounts/registration_pending.html')

class CustomLoginView(LoginView):
    template_name = 'account/login.html'

    def form_valid(self, form):
        user = form.get_user()
        
        # Get the 'next' parameter from the request (if available)
        next_url = self.request.GET.get('next', None)

        if user.is_authenticated:
            # If user is admin, redirect to admin_dashboard
            if user.role == 'administrator':
                return redirect('admin_dashboard')
            
            # If user has not completed their profile, redirect to complete_profile
            elif not user.profile_completed:
                return redirect('complete_profile')
            
            # If no 'next' parameter exists, fallback to dashboard
            if next_url:
                return redirect(next_url)  # Redirect to the intended page
            
            return redirect('dashboard')  # Default redirect to dashboard for captains or crew

        return super().form_valid(form)

# Custom signup view
class CustomSignupView(SignupView):
    def form_valid(self, form):
        # Save the user to the database
        user = form.save(self.request)
        # Redirect to registration_pending
        return redirect(reverse('registration_pending'))

# Administrator dashboard view
@login_required
def admin_dashboard(request):
    if request.user.role == User.ADMINISTRATOR:
        # Filter for users with roles Crew and Captain, excluding superuser and Administrator accounts
        users = User.objects.filter(role__in=[User.CAPTAIN, User.CREW], is_superuser=False).order_by('is_active')
        return render(request, 'accounts/admin_dashboard.html', {'users': users})
    else:
        return redirect('dashboard')  # Redirect non-administrators to their own dashboard

# Custom logout view
class CustomLogoutView(LogoutView):
    next_page = '/'  # Redirect to home page after logout

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('dashboard')  # Redirect to dashboard after updating
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, 'accounts/update_profile.html', {'form': form})

class CrewBookingStatusForm(forms.ModelForm):
    class Meta:
        model = CrewBooking
        fields = ['status']

@login_required
def crew_profile(request, user_id, trip_id):
    crew_member = get_object_or_404(User, id=user_id)
    crew_booking = get_object_or_404(CrewBooking, user=crew_member, trip_id=trip_id)

    if request.method == 'POST':
        form = CrewBookingStatusForm(request.POST, instance=crew_booking)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to dashboard or another page as appropriate
    else:
        form = CrewBookingStatusForm(instance=crew_booking)

    return render(request, 'accounts/crew_profile.html', {
        'crew_member': crew_member,
        'form': form
    })