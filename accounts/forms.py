from allauth.account.forms import SignupForm
from django import forms
from .models import User

class CustomSignupForm(SignupForm):
    ROLE_CHOICES = [
        (User.CAPTAIN, 'Captain'),
        (User.CREW, 'Crew'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    def custom_signup(self, request, user):
        # Set custom fields on the user instance after the initial save
        user.role = self.cleaned_data['role']
        user.is_active = False  # Set the user as inactive initially
        user.profile_completed = False  # Mark profile as incomplete
        user.save()  # Save the updated user instance
        return user


class ProfileCompletionForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="New Password",
        required=False,
        help_text="Leave blank if you don't want to change the password."
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'experience_level', 'password']
        help_texts = {
            'username': None,  # Hides default help text
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the username and email fields read-only
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        user = super().save(commit=False)
        # Only update the password if a new password is provided
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user