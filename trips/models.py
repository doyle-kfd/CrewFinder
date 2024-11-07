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
        limit_choices_to={'role': 'captain'}  # Ensure lowercase "captain" matches your role setup
    )
    crew_needed = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} on {self.date}"

    def formatted_duration(self):
        """Returns a human-readable version of the duration."""
        total_seconds = self.duration.total_seconds()
        days = int(total_seconds // (24 * 3600))
        hours = int((total_seconds % (24 * 3600)) // 3600)
        minutes = int((total_seconds % 3600) // 60)

        if days > 0:
            return f"{days} day(s), {hours} hour(s)"
        elif hours > 0:
            return f"{hours} hour(s), {minutes} minute(s)"
        else:
            return f"{minutes} minute(s)"
