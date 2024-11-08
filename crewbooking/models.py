from django.db import models
from django.conf import settings
from trips.models import Trip  # Import the Trip model

class CrewBooking(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)  # Link to the Trip
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to the User
    status = models.CharField(max_length=10, choices=[
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled')
    ])

    def __str__(self):
        return f"{self.user.username} - {self.trip.title} ({self.status})"