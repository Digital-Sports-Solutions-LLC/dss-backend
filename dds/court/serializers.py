from rest_framework import serializers
from .models import COURT
from event.serializers import EventSerializer

class CourtSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    class Meta:
        model = COURT
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
                
        # Check if 'link' is None and set it to "n/a" if it is
        if representation.get('link') is None:
            representation['link'] = "n/a"
                
        return representation