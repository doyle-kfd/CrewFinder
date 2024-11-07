from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    CAPTAIN = 'captain'
    CREW = 'crew'
    ADMINISTRATOR = 'administrator'

    ROLE_CHOICES = [
        (CAPTAIN, 'Captain'),
        (CREW, 'Crew'),
        (ADMINISTRATOR, 'Administrator'),
    ]

    PENDING = 'pending'
    APPROVED = 'approved'
    DISAPPROVED = 'disapproved'

    APPROVAL_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (DISAPPROVED, 'Disapproved'),
    ]

    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=CREW)
    bio = models.TextField(blank=True, null=True)
    experience_level = models.CharField(max_length=50, blank=True, null=True)
    approval_status = models.CharField(max_length=15, choices=APPROVAL_STATUS_CHOICES, default=PENDING)
    profile_completed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False, help_text="Designates whether a user should be treated as active. Unselect this instead of deleting accounts.")   