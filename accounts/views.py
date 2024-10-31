from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileCompletionForm

# Create your views here.
@login_required
def complete_profile(request):
    if not request.user.is_approved:
        return redirect('dashboard')  # Redirect if user is not approved

    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileCompletionForm(instance=request.user)

    return render(request, 'accounts/complete_profile.html', {'form': form})