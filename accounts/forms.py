from allauth.account.forms import SignupForm
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from .models import User

class CustomSignupForm(SignupForm):
    ROLE_CHOICES = [    
        (User.CAPTAIN, 'Captain'),
        (User.CREW, 'Crew'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.role = self.cleaned_data['role']
        user.is_approved = False  # User is initially unapproved
        user.save()
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

    def save(self, commit=True):
        user = super().save(commit=False)
        # Only update the password if a new password is provided
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user