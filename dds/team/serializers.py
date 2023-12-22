from rest_framework import serializers
from .models import TEAM
from league.serializers import LeagueSerializer
from location.serializers import LocationSerializer


class TeamSerializer(serializers.ModelSerializer):
    league = LeagueSerializer()
    location = LocationSerializer()
    class Meta:
        model = TEAM
        fields = '__all__'
        league = None
        location = None
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Check if 'graphic' is None and set it to a default value if it is
        if representation['graphic'] is None:
            request = self.context.get('request')
            if request is not None:
                domain = request.get_host()
                representation['graphic'] = f"http://{domain}/media/images/file-not-found.jpg"
                
        # Check if 'year_disbanded' is None and set it to "n/a" if it is
        if representation.get('yearDisbanded') is None:
            representation['yearDisbanded'] = "n/a"
                
        return representation
