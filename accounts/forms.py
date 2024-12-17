"""
Forms
This module defines custom forms for user registration, profile management,
and administrative tasks. These forms extend or customize Django's built-in
form functionality to meet the specific needs of the application.

Forms:
1. CustomSignupForm: Extends the Allauth signup form to include
   role selection.
2. ProfileCompletionForm: Allows users to complete their profile with
   fields for
   bio, experience, and profile photo.
3. EditUserForm: Provides administrators with the ability to edit user
   details,
   excluding certain fields from being editable.
4. CrewBookingStatusForm: Enables captains to update the status of a crew
   booking.

Key Features:
- Role-based user registration via the signup form.
- Profile completion with restricted field editing for existing data.
- Administrative editing of user details and role-based status updates.

Dependencies:
- Django forms framework.
- Django Allauth for custom signup functionality.
- Models for User and CrewBooking.
"""

from allauth.account.forms import SignupForm
from django import forms
from .models import User
from crewbooking.models import CrewBooking  # Import CrewBooking model


class CustomSignupForm(SignupForm):
    """
    Custom signup form to include additional fields or logic during signup.
    """

    def __init__(self, *args, **kwargs):
        """
        Accept the 'request' keyword argument as required by Allauth views.
        """
        self.request = kwargs.pop('request', None)  # Extract 'request'
        super().__init__(*args, **kwargs)  # Call parent class __init__

    def save(self, request):
        """
        Save method to handle additional logic after user creation.
        """
        user = super().save(request)  # Call parent save method
        # Add any custom logic here if needed
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
            'username': None,
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
