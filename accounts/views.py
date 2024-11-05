from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ProfileCompletionForm
from allauth.account.views import SignupView
from django.urls import reverse

# Profile completion view
@login_required
def complete_profile(request):
    if request.user.profile_completed:
        return redirect('dashboard')  # Redirect if profile is already complete

    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            request.user.profile_completed = True
            request.user.save()
            return redirect('dashboard')  # Redirect to dashboard after profile completion
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, 'accounts/complete_profile.html', {'form': form})

# Dashboard view
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

# Registration pending view
def registration_pending(request):
    return render(request, 'accounts/registration_pending.html')

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'account/login.html'  # Replace with your actual login template

    def form_valid(self, form):
        # Call the original form_valid method
        response = super().form_valid(form)
        # Check if the authenticated user has completed their profile
        if self.request.user.is_authenticated and not self.request.user.profile_completed:
            return redirect('complete_profile')
        return response

class CustomSignupView(SignupView):
    def form_valid(self, form):
        # Save the user to the database
        user = form.save(self.request)  # Allauth expects only `request` as an argument
        # Redirect to registration_pending
        return redirect(reverse('registration_pending'))