from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileCompletionForm

# Create your views here.
@login_required
def complete_profile(request):
    if not request.user.is_approved:
        return redirect('registration_complete')  # Redirect unapproved users

    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to dashboard after profile completion
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, 'accounts/complete_profile.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def registration_pending(request):
    return render(request, 'accounts/registration_pending.html')


def custom_login_view(request, *args, **kwargs):
    response = login(request, *args, **kwargs)
    if request.user.is_authenticated and not request.user.profile_completed:
        return redirect('complete_profile')
    return response