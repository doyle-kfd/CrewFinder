"""
Models for the crewbooking app.

This module defines the data structure for crew bookings
in the CrewFinder application.
The `CrewBooking` model links users to trips,
allowing them to apply and track the
status of their applications.

Classes:
- CrewBooking: Represents a user's application for a trip,
  including status tracking.

"""

from django.db import models
from django.conf import settings
from trips.models import Trip  # Import the Trip model


class CrewBooking(models.Model):
    """
    Represents an application made by a user (crew member)
    for a specific trip.

    Fields:
    - trip (ForeignKey): References the `Trip` model to link a
      booking to a trip.
      Deletes related bookings when the trip is deleted.
    - user (ForeignKey): References the `AUTH_USER_MODEL`
      to link a booking to a user.
      Deletes related bookings when the user is deleted.
    - status (CharField): Tracks the application status with choices:
        - 'confirmed': The application is approved.
        - 'pending': The application is awaiting approval (default).
        - 'declined': The application is declined.

    Attributes:
    - _original_status (str): Stores the initial status of
       the booking instance
       to allow tracking of changes.

    Methods:
    - save(*args, **kwargs): Overrides the default save method
      to update `_original_status`
      after saving.
    - __str__(): Returns a string representation of the booking,
      including the user,
      trip, and application status.
    """

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        help_text="The trip this booking is associated with."
    )  # Link to the Trip
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="The user who applied for this trip."
    )  # Link to the User
    status = models.CharField(
        max_length=10,
        choices=[
            ('confirmed', 'Confirmed'),
            ('pending', 'Pending'),
            # Changed from 'cancelled' to 'declined'
            ('declined', 'Declined'),
        ],
        default='pending',
        help_text="The status of the booking application."
    )

    def __init__(self, *args, **kwargs):
        """
        Initializes the CrewBooking instance.

        Overrides the default initialization to store the
        initial status of the booking
        for tracking purposes.
        """
        super().__init__(*args, **kwargs)
        self._original_status = self.status  # Store the initial status

    def save(self, *args, **kwargs):
        """
        Saves the CrewBooking instance.

        Overrides the default save method to update
        `_original_status` after saving,
        ensuring it reflects the most recent status of the booking.
        """
        super().save(*args, **kwargs)
        # Update _original_status after saving
        self._original_status = self.status

    def __str__(self):
        """
        Returns a string representation of the booking.

        Format:
        - `<username> applied for <trip_title> - Status: <status>`
        """
        return (f"{self.user.username} applied for {self.trip.title} -  "
                f"Status: {self.status}")
