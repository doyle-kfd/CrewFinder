from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ProfileCompletionForm
from .models import User  # Ensure you import the User model here
from allauth.account.views import SignupView
from django.urls import reverse
import logging

# Set up a logger for the views module
logger = logging.getLogger(__name__)

# Profile completion view
@login_required
def complete_profile(request):
    if request.user.profile_completed:
        logger.info("Profile already complete. Redirecting to dashboard.")
        return redirect('dashboard')  # Redirect if profile is already complete

    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            request.user.profile_completed = True
            request.user.save()
            logger.info(f"Profile completed for user: {request.user.username}")
            return redirect('dashboard')  # Redirect to dashboard after profile completion
    else:
        form = ProfileCompletionForm(instance=request.user)
        logger.debug("Rendering profile completion form.")

    return render(request, 'accounts/complete_profile.html', {'form': form})

# Dashboard view
@login_required
def dashboard(request):
    # Redirect administrators to their custom dashboard
    if request.user.role == User.ADMINISTRATOR:
        logger.info(f"Administrator {request.user.username} accessing admin dashboard.")
        return redirect('admin_dashboard')
    logger.info(f"User {request.user.username} accessing regular dashboard.")
    return render(request, 'accounts/dashboard.html')

# Registration pending view
def registration_pending(request):
    logger.info("Rendering registration pending page.")
    return render(request, 'accounts/registration_pending.html')

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'account/login.html'

    def form_valid(self, form):
        user = self.request.user
        logger.info(f"Login attempt by user: {user.username}")
        if user.is_authenticated:
            if user.role == User.ADMINISTRATOR:
                logger.info("Redirecting administrator to admin dashboard.")
                return redirect('admin_dashboard')
            elif not user.profile_completed:
                logger.info("Redirecting user to complete profile page.")
                return redirect('complete_profile')
        # Fallback to the default LOGIN_REDIRECT_URL
        return super().form_valid(form)

# Custom signup view
class CustomSignupView(SignupView):
    def form_valid(self, form):
        # Save the user to the database
        user = form.save(self.request)  # Allauth expects only `request` as an argument
        logger.info(f"New user signed up: {user.username}. Redirecting to registration pending.")
        # Redirect to registration_pending
        return redirect(reverse('registration_pending'))

# Administrator dashboard view
@login_required
def admin_dashboard(request):
    # Check if the logged-in user is an Administrator
    if request.user.role == User.ADMINISTRATOR:
        logger.info(f"Administrator {request.user.username} accessing admin dashboard.")
        # Filter for users with roles Crew and Captain, excluding superuser and Administrator accounts
        users = User.objects.filter(role__in=[User.CAPTAIN, User.CREW], is_superuser=False).order_by('is_active')
        return render(request, 'accounts/admin_dashboard.html', {'users': users})
    else:
        logger.warning(f"Non-administrator user {request.user.username} attempted to access admin dashboard.")
        # Redirect non-administrators to their own dashboard or another page
        return redirect('dashboard')
