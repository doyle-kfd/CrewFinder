from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProfileCompletionForm
from .models import User
from allauth.account.views import SignupView

# Profile completion view
@login_required
def complete_profile(request):
    if request.user.profile_completed:
        return redirect('dashboard')  # Redirect if profile is already complete

    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()  # Save form fields
            request.user.profile_completed = True
            request.user.save(update_fields=['profile_completed'])  # Save only `profile_completed`

            # Ensure the user session remains active after completing profile
            request.session.modified = True
            return redirect('dashboard')  # Redirect to dashboard after profile completion
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, 'accounts/complete_profile.html', {'form': form})

# Dashboard view
@login_required
def dashboard(request):
    # Redirect administrators to their custom dashboard
    if request.user.role == User.ADMINISTRATOR:
        return redirect('admin_dashboard')
    return render(request, 'accounts/dashboard.html')

# Registration pending view
def registration_pending(request):
    return render(request, 'accounts/registration_pending.html')

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'account/login.html'

    def form_valid(self, form):
        user = self.request.user
        if user.is_authenticated:
            if user.role == User.ADMINISTRATOR:
                return redirect('admin_dashboard')
            elif not user.profile_completed:
                return redirect('complete_profile')
        return super().form_valid(form)  # Default fallback if not redirected

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
    # Check if the logged-in user is an Administrator
    if request.user.role == User.ADMINISTRATOR:
        # Filter for users with roles Crew and Captain, excluding superuser and Administrator accounts
        users = User.objects.filter(role__in=[User.CAPTAIN, User.CREW], is_superuser=False).order_by('is_active')
        return render(request, 'accounts/admin_dashboard.html', {'users': users})
    else:
        # Redirect non-administrators to their own dashboard or another page
        return redirect('dashboard')

# Custom logout view
class CustomLogoutView(LogoutView):
    next_page = '/'  # Redirect to home page after logout

    def dispatch(self, request, *args, **kwargs):
        # Add a logout success message
        messages.success(request, "You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)
