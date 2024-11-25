from django.test import TestCase
from accounts.models import User


class UserModelTest(TestCase):
    """
    Test suite for the custom User model in the 'accounts' app.

    This test suite covers:
    - Default field values and their correctness.
    - Role and approval status behavior.
    - String representation of the User model.
    - Handling of the experience field and profile photo field.
    """

    def setUp(self):
        """
        Set up test data for the User model tests.

        Creates:
        - Three users with roles: captain, crew, and administrator.
        - Users have different approval statuses for testing.
        """
        self.captain_user = User.objects.create(
            username='captain_user',
            role=User.CAPTAIN,
            approval_status=User.APPROVED,
        )
        self.crew_user = User.objects.create(
            username='crew_user',
            role=User.CREW,
            approval_status=User.PENDING,
        )
        self.admin_user = User.objects.create(
            username='admin_user',
            role=User.ADMINISTRATOR,
            approval_status=User.DISAPPROVED,
        )

    def test_default_values(self):
        """
        Test that default values for the User model are set correctly.

        Ensures that:
        - Role defaults to 'crew'.
        - Approval status defaults to 'pending'.
        - `is_active` defaults to False.
        - Experience level defaults to 'None'.
        """
        user = User.objects.create(username='test_user')
        self.assertEqual(user.role, User.CREW)
        self.assertEqual(user.approval_status, User.PENDING)
        self.assertFalse(user.is_active)
        self.assertEqual(user.experience, 'None')

    def test_role_choices(self):
        """
        Test that the role field correctly stores and retrieves role choices.

        Ensures that:
        - The role field accepts 'captain', 'crew', and 'administrator'.
        """
        self.assertEqual(self.captain_user.role, User.CAPTAIN)
        self.assertEqual(self.crew_user.role, User.CREW)
        self.assertEqual(self.admin_user.role, User.ADMINISTRATOR)

    def test_approval_status_behavior(self):
        """
        Test that the `is_active` field is updated based on the `approval_status` field.

        Ensures that:
        - Approved users have `is_active=True`.
        - Pending or disapproved users have `is_active=False`.
        - Changes to `approval_status` dynamically update `is_active`.
        """
        # Check active status for approved user
        self.assertTrue(self.captain_user.is_active)

        # Check active status for pending user
        self.assertFalse(self.crew_user.is_active)

        # Check active status for disapproved user
        self.assertFalse(self.admin_user.is_active)

        # Change approval status and verify `is_active` updates
        self.crew_user.approval_status = User.APPROVED
        self.crew_user.save()
        self.assertTrue(self.crew_user.is_active)

        self.captain_user.approval_status = User.DISAPPROVED
        self.captain_user.save()
        self.assertFalse(self.captain_user.is_active)

    def test_experience_choices(self):
        """
        Test that the experience field accepts valid choices.

        Ensures that:
        - Valid experience levels (e.g., 'RYA Dayskipper') are correctly stored.
        """
        user = User.objects.create(username='experienced_user', experience='RYA Dayskipper')
        self.assertEqual(user.experience, 'RYA Dayskipper')

    def test_string_representation(self):
        """
        Test the string representation of the User model.

        Ensures that:
        - The `__str__()` method returns the username.
        """
        self.assertEqual(str(self.captain_user), 'captain_user')
        self.assertEqual(str(self.crew_user), 'crew_user')
        self.assertEqual(str(self.admin_user), 'admin_user')

    def test_profile_photo_field(self):
        """
        Test that the profile photo field can be left blank or updated.

        Ensures that:
        - The `photo` field is None by default.
        - The `photo` field can be updated with a valid file path.
        """
        user = User.objects.create(username='photo_user')
        self.assertIsNone(user.photo)
        user.photo = 'path/to/photo.jpg'
        user.save()
        self.assertEqual(user.photo, 'path/to/photo.jpg')
