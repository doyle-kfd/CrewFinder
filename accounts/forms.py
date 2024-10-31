from allauth.account.forms import SignupForm
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