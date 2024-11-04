# Extend class to create custom user model
from django.contrib.auth.models import AbstractUser 
from django.db import models

# Create your models here.
class User(AbstractUser):
    CAPTAIN = 'captain'
    CREW = 'crew'
    ROLE_CHOICES = [
        (CAPTAIN, 'Captain'),
        (CREW, 'Crew'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CREW)
    bio = models.TextField(blank=True, null=True)
    experience_level = models.CharField(max_length=50, blank=True, null=True)
    is_approved = models.BooleanField(default=False)  # Approval status
    profile_completed = models.BooleanField(default=False)  # New field to track completion