from rest_framework import serializers
from .models import COURT
from event.serializers import EventSerializer

class CourtSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    class Meta:
        model = COURT
        exclude = ('event')