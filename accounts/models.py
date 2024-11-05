# Extend class to create custom user model
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    CAPTAIN = 'captain'
    CREW = 'crew'
    ADMINISTRATOR = 'administrator'  # Rename project_admin to administrator

    ROLE_CHOICES = [
        (CAPTAIN, 'Captain'),
        (CREW, 'Crew'),
        (ADMINISTRATOR, 'Administrator'),
    ]

    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=CREW)
    bio = models.TextField(blank=True, null=True)
    experience_level = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=False)  # Default to inactive for new users
    profile_completed = models.BooleanField(default=False)
