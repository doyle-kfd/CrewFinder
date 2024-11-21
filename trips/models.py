from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

class Trip(models.Model):
    title = models.CharField(max_length=100)
    departing_from = models.CharField(max_length=100)
    arriving_at = models.CharField(max_length=100)
    departure_date = models.DateField()
    duration = models.DurationField()
    boat_name = models.CharField(max_length=100)
    boat_description = models.TextField(blank=True, null=True)
    trip_description = models.TextField(blank=True, null=True)
    captain = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'Captain'}
    )
    crew_needed = models.PositiveIntegerField()
    boat_image = CloudinaryField('image', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Assign default image if none is provided
        if not self.boat_image:
            self.boat_image = 'default_boat_fkc4gr'  # Default Boat
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} on {self.departure_date}"

    def formatted_duration(self):
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
