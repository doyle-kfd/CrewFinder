"""
Models
This module defines the models for the application, including
a custom user model
that extends Django's `AbstractUser` to add additional fields and
functionality
required for user roles, profile management, and approval workflows.

Models:
1. User: Extends the `AbstractUser` model to include roles
         (Captain, Crew, Administrator),
         approval statuses, sailing experience, profile completion,
         and profile photos.

Key Features:
- Role-based user management (Captain, Crew, Administrator).
- Profile completion and approval workflows.
- Sailing experience levels and custom attributes.
- Integration with Cloudinary for profile photos.

Dependencies:
- Django's built-in `AbstractUser` for user management.
- Cloudinary for storing profile photos.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField  # For Cloudinary integration


class User(AbstractUser):
    """
    Custom user model extending AbstractUser to include additional fields and
    functionality.

    Attributes:
        ROLE_CHOICES (list): Choices for user roles (Captain, Crew,
            Administrator).
        APPROVAL_STATUS_CHOICES (list): Choices for user approval statuses
            (Pending, Approved, Disapproved).
        EXPERIENCE_CHOICES (list): Choices for user sailing experience levels.
        email (EmailField): Email address of the user, must be unique.
        role (str): Role of the user, default is 'crew'.
        bio (TextField): User's biography, optional.
        experience_level (str): Legacy field for experience level, optional.
        approval_status (str): Approval status of the user, default is
            'pending'.
        profile_completed (bool): Indicates whether the user has completed
            their profile.
        is_active (bool): Indicates if the user account is active, determined
            by approval status.
        experience (str): Sailing experience level of the user, default is
            'None'.
        photo (CloudinaryField): Profile photo stored in Cloudinary, optional.
    """

    # Role Choices
    CAPTAIN = 'captain'
    CREW = 'crew'
    ADMINISTRATOR = 'administrator'

    ROLE_CHOICES = [
        (CAPTAIN, 'Captain'),
        (CREW, 'Crew'),
        (ADMINISTRATOR, 'Administrator'),
    ]

    # Approval Status Choices
    PENDING = 'pending'
    APPROVED = 'approved'
    DISAPPROVED = 'disapproved'

    APPROVAL_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (DISAPPROVED, 'Disapproved'),
    ]

    # Experience Choices
    EXPERIENCE_CHOICES = [
        ('None', 'None'),
        ('RYA Competent Crew', 'RYA Competent Crew'),
        ('RYA Dayskipper', 'RYA Dayskipper'),
        ('RYA Yachtmaster Coastal', 'RYA Yachtmaster Coastal'),
        ('RYA Yachtmaster Offshore', 'RYA Yachtmaster Offshore'),
        ('RYA Yachtmaster Ocean', 'RYA Yachtmaster Ocean'),
    ]

    # Custom Fields
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        help_text="Email address is required and must be unique.",
    )

    role = models.CharField(
        max_length=15, choices=ROLE_CHOICES, default=CREW
    )
    bio = models.TextField(blank=True, null=True)
    experience_level = models.CharField(
        max_length=50, blank=True, null=True
    )  # Legacy field
    approval_status = models.CharField(
        max_length=15, choices=APPROVAL_STATUS_CHOICES, default=PENDING
    )
    profile_completed = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=False,
        help_text=(
            "Designates whether a user should be treated as active. Unselect "
            "this instead of deleting accounts."
        )
    )
    experience = models.CharField(
        max_length=100, choices=EXPERIENCE_CHOICES, default='None'
    )
    photo = CloudinaryField('photo', blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Overrides the save method to automatically
        update the `is_active` field
        based on the `approval_status`.

        If the `approval_status` is 'approved', the
        `is_active` field is set to
        True. If the `approval_status` is 'pending' or 'disapproved', the
        `is_active` field is set to False.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if self.approval_status == self.APPROVED:
            self.is_active = True
        elif self.approval_status in [self.DISAPPROVED, self.PENDING]:
            self.is_active = False
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns the string representation of the user, which is the username.

        Returns:
            str: The username of the user.
        """
        return self.username
