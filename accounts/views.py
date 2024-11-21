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
from django.db.models import Count
from .forms import EditUserForm  # Assume you have a form for editing user details
from cloudinary.models import CloudinaryField

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
    # Redirect administrator users
    if request.user.role == User.ADMINISTRATOR:
        return redirect('admin_dashboard')

    # For captains, fetch their trips and associated applications
    if request.user.role == 'captain':
        # Get trips created by the captain
        my_trips = Trip.objects.filter(captain=request.user).annotate(applicant_count=Count('crewbooking')).order_by('-departure_date')
        
        # Get all applications for those trips
        applied_crews = CrewBooking.objects.filter(trip__in=my_trips).select_related('user', 'trip')

        return render(request, 'accounts/dashboard.html', {
            'my_trips': my_trips,
            'applied_crews': applied_crews,
        })

    # For crew members, show trips they applied for
    elif request.user.role == 'crew':
        applied_trips = CrewBooking.objects.filter(user=request.user).select_related('trip')

        return render(request, 'accounts/dashboard.html', {
            'applied_trips': applied_trips,
        })

    # Raise permission error for invalid roles
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
        # Add request.FILES to handle file uploads
        form = ProfileCompletionForm(request.POST, request.FILES, instance=request.user)
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
            return redirect('dashboard')  # Redirect as needed
    else:
        form = CrewBookingStatusForm(instance=crew_booking)

    return render(request, 'accounts/crew_profile.html', {
        'crew_member': crew_member,
        'form': form
    })

@login_required
def edit_user(request, user_id):
    if request.user.role != 'administrator':  # Custom role check
        return redirect('dashboard')

    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Save form and let the model's save() handle is_active
            return redirect('admin_dashboard')
    else:
        form = EditUserForm(instance=user)

    return render(request, 'accounts/edit_user.html', {'form': form, 'user_obj': user})