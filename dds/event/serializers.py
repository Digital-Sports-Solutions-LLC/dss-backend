from rest_framework import serializers
from .models import EVENT
from season.serializers import SeasonSerializer
from league.serializers import LeagueSerializer
from location.serializers import LocationSerializer
from event_type.serializers import Event_TypeSerializer


class EventSerializer(serializers.ModelSerializer):
    season = SeasonSerializer()
    league = LeagueSerializer()
    location = LocationSerializer()
    event_type = Event_TypeSerializer()
    
    class Meta:
        model = EVENT
        fields = '__all__'
        season = None
        league = None
        location = None
        event_type = None
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Check if 'graphic' is None and set it to a default value if it is
        if representation['graphic'] is None:
            request = self.context.get('request')
            if request is not None:
                domain = request.get_host()
                representation['graphic'] = f"http://{domain}/media/images/file-not-found.jpg"
    
        return representation