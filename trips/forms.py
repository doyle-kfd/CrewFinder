from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        # Include all fields except `captain` which will be set automatically in the view
        fields = ['title', 'location', 'date', 'duration', 'crew_needed']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Adds a date picker for the date field
        }
        help_texts = {
            'title': 'Enter a unique title for the trip',
            'location': 'Specify the location of the trip',
            'date': 'Select the date for the trip',
            'duration': 'Enter the duration of the trip in hours or days',
            'crew_needed': 'Specify the number of crew members required',
        }
