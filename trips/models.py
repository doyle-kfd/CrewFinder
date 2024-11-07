from django.db import models
from django.conf import settings

class Trip(models.Model):
    title = models.CharField(max_length=100, help_text="Name of the trip")
    location = models.CharField(max_length=100, help_text="Location where the trip will take place")
    date = models.DateField(help_text="Date of the trip")
    duration = models.PositiveIntegerField(help_text="Duration of the trip in hours")  # specify hours or days
    captain = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'Captain'},  # Limits to Captain role users
        related_name='trips',
        help_text="Captain organizing the trip"
    )
    crew_needed = models.PositiveIntegerField(help_text="Number of crew members needed")

    def __str__(self):
        return self.title
