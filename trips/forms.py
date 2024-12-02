"""
Forms for managing trips in the CrewFinder application.

This module defines forms for creating and editing trips.
It includes custom widgets, placeholders, and validation logic to ensure
user-friendly and accurate data entry.

Classes:
- TripCreationForm: A form for captains to create or edit
  trips with customized fields and validation.
"""

from django import forms
from .models import Trip
from datetime import timedelta


class TripCreationForm(forms.ModelForm):
    """
    A form for creating or editing a trip.

    Features:
    - Custom widgets with placeholders for enhanced user experience.
    - Custom validation for the `duration` field to handle natural
      language input (e.g., "5 hours", "2 days").

    Fields:
    - title: The title of the trip.
    - departing_from: The trip's departure location.
    - arriving_at: The trip's destination.
    - departure_date: The trip's start date.
    - duration: The duration of the trip, validated to accept
                natural language.
    - crew_needed: The number of crew members required for the trip.
    - boat_name: The name of the boat.
    - boat_description: A description of the boat.
    - trip_description: A description of the trip.
    - boat_image: An optional image of the boat.

    Methods:
    - clean_duration(): Validates and converts the `duration` input into a
      `timedelta` object.
    """

    duration = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g., 5 hours or 2 days'
        }),
        help_text="Enter the trip duration in "
                  "hours or days (e.g., '5 hours' or '2 days')."
    )

    class Meta:
        """
        Meta options for the TripCreationForm.

        Attributes:
        - model: The model associated with the form (Trip).
        - fields: The fields included in the form.
        - widgets: Custom widgets for specific fields to enhance
                   the form's appearance and usability.
        """
        model = Trip
        fields = [
            'title',
            'departing_from',
            'arriving_at',
            'departure_date',
            'duration',
            'crew_needed',
            'boat_name',
            'boat_description',
            'trip_description',
            'boat_image',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'departing_from':  forms.TextInput(attrs={'placeholder':
                                                      'Departing From'}),
            'arriving_at':   forms.TextInput(attrs={'placeholder':
                                                    'Arriving At'}),
            'departure_date': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'Departure Date'
            }),
            'crew_needed':
                forms.NumberInput(attrs={'placeholder': 'Crew Needed'}),
            'boat_name': forms.TextInput(attrs={'placeholder': 'Boat Name'}),
            'boat_description': forms.Textarea(attrs={
                'placeholder': 'Description of the boat',
                'rows': 3
            }),
            'trip_description': forms.Textarea(attrs={
                'placeholder': 'Description of the trip',
                'rows': 3
            }),
            'boat_image':
                forms.
                ClearableFileInput(attrs={'placeholder': 'Upload Boat Image'}),
        }

    def clean_duration(self):
        """
        Validates and processes the `duration` input.

        Converts user-friendly duration input
        (e.g., "5 hours", "2 days") into a `timedelta` object.

        Returns:
        - timedelta: The parsed duration as a `timedelta` object.

        Raises:
        - forms.ValidationError: If the input format
                                 is invalid or cannot be parsed.

        Example Valid Inputs:
        - "5 hours" → timedelta(hours=5)
        - "2 days" → timedelta(days=2)

        Example Invalid Inputs:
        - "5"
        - "two days"
        """
        duration_input = self.cleaned_data['duration'].strip().lower()
        try:
            if "hour" in duration_input:
                hours = int(duration_input.split()[0])
                return timedelta(hours=hours)
            elif "day" in duration_input:
                days = int(duration_input.split()[0])
                return timedelta(days=days)
            else:
                raise ValueError("Invalid format")
        except ValueError:
            raise forms.ValidationError("Enter a valid duration,"
                                        " e.g., '5 hours' or '2 days'")
