from allauth.account.forms import SignupForm
from django import forms
from .models import User

class CustomSignupForm(SignupForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, required=True)

    def custom_signup(self, request, user):
        user.role = self.cleaned_data['role']
        user.is_active = False
        user.profile_completed = False
        user.save()
        return user

class ProfileCompletionForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'experience', 'photo']  # Use 'experience' and 'photo'
        help_texts = {
            'username': None,  # Remove default help text for the username field
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make username and email fields read-only
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        user = super().save(commit=False)
        # Save without modifying the password
        if commit:
            user.save()
        return user

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'approval_status', 'experience', 'photo']