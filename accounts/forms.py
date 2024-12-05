from allauth.account.forms import SignupForm
from django import forms
from .models import User


from django import forms
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from .models import User  # Adjust the import path as per your project structure

from django import forms
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from .models import User  # Adjust the import path as per your project structure

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

    Meta:
        model (User): The User model associated with the form.
        fields (list): Fields included in the form ('username', 'email',
        'bio', 'experience', 'photo').
        help_texts (dict): Removes default help text for the username field.

    Methods:
        __init__(*args, **kwargs): Initializes the form and makes the
        username and email fields read-only.
        save(commit=True): Saves the form without modifying the user's
        password.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'experience', 'photo']
        help_texts = {
            # Remove default help text for the username field
            'username': None,
                    }

    def __init__(self, *args, **kwargs):
        """
        Initializes the form and sets the username and email fields
        to read-only.
        """
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        """
        Saves the form data to the user instance without modifying the
        password.

        Args:
            commit (bool): Whether to save the user instance immediately.

        Returns:
            User: The updated user instance.
        """
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class EditUserForm(forms.ModelForm):
    """
    Form for administrators to edit user details, including role, approval
    status, experience, and profile photo.

    Meta:
        model (User): The User model associated with the form.
        fields (list): Fields included in the form ('username', 'email',
        'role', 'approval_status', 'experience', 'photo').
    """
    class Meta:
        model = User
        fields = [
            'username', 'email', 'role', 'approval_status', 'experience',
            'photo'
        ]
