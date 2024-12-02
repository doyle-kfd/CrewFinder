"""
Model for managing trips in the CrewFinder application.

This module defines the `Trip` model, which represents sailing trips
created by captains.
The model includes fields for trip details, relationships to captains,
and functionality
to calculate formatted durations and handle default images.

Classes:
- Trip: Represents a sailing trip with its associated details
        and functionality.
"""

from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


class Trip(models.Model):
    """
    Represents a sailing trip in the CrewFinder application.

    Fields:
    - title (CharField): The title or name of the trip.
    - departing_from (CharField): The departure location for the trip.
    - arriving_at (CharField): The arrival location for the trip.
    - departure_date (DateField): The date the trip departs.
    - duration (DurationField): The duration of the trip (e.g., days, hours).
    - boat_name (CharField): The name of the boat used for the trip.
    - boat_description (TextField): Optional description of the boat.
    - trip_description (TextField): Optional description of the trip.
    - captain (ForeignKey): Links the trip to a user with the role of
                            "Captain."
    - crew_needed (PositiveIntegerField): The number of crew members needed
                                          for the trip.
    - boat_image (CloudinaryField): Optional image of the boat,
                                    stored using Cloudinary.

    Methods:
    - save(*args, **kwargs): Overrides the save method to assign a
                             default boat image if none is provided.
    - __str__(): Returns a string representation of the trip,
                 including the title and departure date.
    - formatted_duration(): Calculates and returns a human-readable
                            string representation of the trip's duration.
    """

    title = models.CharField(max_length=100,  help_text="The title or name "
                                                        "of the trip.")
    departing_from = models.CharField(max_length=100,
                                      help_text="The departure location.")
    arriving_at = models.CharField(max_length=100,
                                   help_text="The arrival location.")
    departure_date = models.DateField(help_text="The departure "
                                                "date of the trip.")
    duration = models.DurationField(help_text="The duration of the trip "
                                    "(days, hours, etc.).")
    boat_name = models.CharField(max_length=100,
                                 help_text="The name of the boat.")
    boat_description = models.TextField(blank=True, null=True,
                                        help_text="Optional description"
                                                  " of the boat.")
    trip_description = models.TextField(blank=True,
                                        null=True, help_text="Optional "
                                                             "description "
                                                             "of the trip.")
    captain = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'Captain'},
        help_text="The captain creating and managing this trip."
    )
    crew_needed = models.PositiveIntegerField(help_text="Number of "
                                                        "crew members"
                                                        " required.")
    boat_image = CloudinaryField('image', blank=True,
                                 null=True, help_text="Optional image"
                                                      " of the boat.")

    def save(self, *args, **kwargs):
        """
        Saves the Trip instance.

        Overrides the default save method to assign a default
        boat image if none is provided.

        Parameters:
        - *args: Variable length argument list.
        - **kwargs: Arbitrary keyword arguments.

        Returns:
        - None
        """
        if not self.boat_image:
            self.boat_image = 'default_boat_fkc4gr'  # Default boat image ID
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the Trip instance.

        Format:
        - "<title> on <departure_date>"

        Example:
        - "Mediterranean Adventure on 2024-12-01"
        """
        return f"{self.title} on {self.departure_date}"

    def formatted_duration(self):
        """
        Formats the duration of the trip into a human-readable string.

        Converts the `duration` field (stored as a `timedelta`)
        into a readable format such as days, hours, and minutes.

        Returns:
        - str: A formatted duration string.

        Examples:
        - "2 day(s), 5 hour(s)"
        - "3 hour(s), 15 minute(s)"
        - "45 minute(s)"
        """
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
