from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField  # For Cloudinary integration

class User(AbstractUser):
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
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=CREW)
    bio = models.TextField(blank=True, null=True)
    experience_level = models.CharField(max_length=50, blank=True, null=True)  # Legacy field
    approval_status = models.CharField(max_length=15, choices=APPROVAL_STATUS_CHOICES, default=PENDING)
    profile_completed = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=False,
        help_text="Designates whether a user should be treated as active. Unselect this instead of deleting accounts."
    )
    experience = models.CharField(max_length=100, choices=EXPERIENCE_CHOICES, default='None')
    photo = CloudinaryField('photo', blank=True, null=True)  # Profile photo stored in Cloudinary

    # Override save() to automatically update is_active based on approval_status
    def save(self, *args, **kwargs):
        if self.approval_status == self.APPROVED:
            self.is_active = True
        elif self.approval_status in [self.DISAPPROVED, self.PENDING]:  # Explicitly handle Pending and Disapproved
            self.is_active = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
