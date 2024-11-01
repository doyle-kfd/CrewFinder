from django.test import TestCase
from accounts.forms import CustomSignupForm

class CustomSignupFormTest(TestCase):
    def test_valid_signup_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'role': 'crew',
        }
        form = CustomSignupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_signup_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'invalid-email',  # Invalid email
            'password1': 'testpassword123',
            'password2': 'wrongpassword',  # Password mismatch
            'role': 'captain',
        }
        form = CustomSignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertIn('password2', form.errors)