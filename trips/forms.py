from django import forms
from .models import Trip
from datetime import timedelta

class TripCreationForm(forms.ModelForm):
    duration = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'e.g., 5 hours or 2 days'
    }))

    class Meta:
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
            'departing_from': forms.TextInput(attrs={'placeholder': 'Departing From'}),
            'arriving_at': forms.TextInput(attrs={'placeholder': 'Arriving At'}),
            'departure_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Departure Date'}),
            'crew_needed': forms.NumberInput(attrs={'placeholder': 'Crew Needed'}),
            'boat_name': forms.TextInput(attrs={'placeholder': 'Boat Name'}),
            'boat_description': forms.Textarea(attrs={'placeholder': 'Description of the boat'}),
            'trip_description': forms.Textarea(attrs={'placeholder': 'Description of the trip'}),
            'boat_image': forms.ClearableFileInput(attrs={'placeholder': 'Upload Boat Image'}),
        }

    def clean_duration(self):
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
            raise forms.ValidationError("Enter a valid duration, e.g., '5 hours' or '2 days'")