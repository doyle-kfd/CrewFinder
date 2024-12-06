from allauth.account.forms import SignupForm
from django import forms
from .models import User
from crewbooking.models import CrewBooking  # Import CrewBooking model


class CustomSignupForm(SignupForm):
    """
    Custom signup form to allow users to select their role during registration.
    """
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, required=True)

    def custom_signup(self, request, user):
        """
        Assigns the selected role to the user and saves the user.
        """
        user.role = self.cleaned_data['role']
        user.email = self.cleaned_data['email']
        user.save()
        return user


class ProfileCompletionForm(forms.ModelForm):
    """
    Form for users to complete their profile, including fields for bio,
    experience, and profile photo.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'experience', 'photo']
        help_texts = {
            'username': None,  # Remove default help text for the username field
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class EditUserForm(forms.ModelForm):
    """
    Form for administrators to edit user details, excluding username and email
    from being editable.
    """
    class Meta:
        model = User
        fields = [
            'username', 'email', 'role', 'approval_status', 'experience',
            'photo'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['email'].disabled = True
        self.fields['role'].disabled = True


class CrewBookingStatusForm(forms.ModelForm):
    """
    Form for captains to update the status of a crew booking.
    """
    class Meta:
        model = CrewBooking
        fields = ['status']
