from django import forms
from .models import Trip
from datetime import timedelta

class TripCreationForm(forms.ModelForm):
    duration = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'e.g., 5 hours or 2 days'
    }))

    class Meta:
        model = Trip
        fields = ['title', 'location', 'date', 'duration', 'crew_needed']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date'}),
            'crew_needed': forms.NumberInput(attrs={'placeholder': 'Crew Needed'}),
        }

    def clean_duration(self):
        """Converts a human-readable duration (e.g., '5 hours') into a timedelta."""
        duration_input = self.cleaned_data['duration'].strip().lower()
        try:
            if "hour" in duration_input:
                hours = int(duration_input.split()[0])
                return timedelta(hours=hours)
            elif "day" in duration_input:
                days = int(duration_input.split()[0])
                return timedelta(days=days)
            # Add more parsing as needed for minutes, weeks, etc.
            else:
                raise ValueError("Invalid format")
        except ValueError:
            raise forms.ValidationError("Enter a valid duration, e.g., '5 hours' or '2 days'")
