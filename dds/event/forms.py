from django import forms
from .models import EVENT

class EventForm(forms.ModelForm):
    class Meta:
        model = EVENT
        fields = ['season', 'league', 'name', 'location', 'startDate', 'endDate', 'event_type', 'graphic']