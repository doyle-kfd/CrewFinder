from django.db import models
from django.conf import settings

class Trip(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    duration = models.DurationField()
    captain = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'Captain'}
    )
    crew_needed = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} on {self.date}"