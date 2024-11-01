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


def registration_complete(request):
    return render(request, 'accounts/registration_complete.html')