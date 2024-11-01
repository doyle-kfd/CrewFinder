from django.urls import reverse
from django.test import TestCase

class SignupViewTest(TestCase):
    def test_signup_view_renders_correct_template(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')