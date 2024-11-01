from django.test import TestCase
from accounts.models import User

class UserModelTest(TestCase):
    def test_user_creation_with_role(self):
        user = User.objects.create_user(
            username='newuser',
            email='newuser@example.com',
            password='testpassword123',
            role='crew'
        )
        self.assertEqual(user.role, 'crew')
        self.assertFalse(user.is_approved)