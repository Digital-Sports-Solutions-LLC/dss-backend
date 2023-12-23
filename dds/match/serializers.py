from rest_framework import serializers
from .models import MATCH
from court.serializers import CourtSerializer
from match_type.serializers import Match_TypeSerializer
from team.serializers import TeamSerializer
from user_ref.serializers import User_RefSerializer

class MatchSerializer(serializers.ModelSerializer):
    court_event = CourtSerializer()
    match_type = Match_TypeSerializer()
    team1 = TeamSerializer()
    team2 = TeamSerializer()
    headRef = User_RefSerializer()
    officiatingTeam = TeamSerializer()

    class Meta:
        model = MATCH
        fields = '__all__'
        court_event = None
        match_type = None
        team1 = None
        team2 = None
        headRef = None
        officiatingTeam = None
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
                
        # Check if 'endTime' is None and set it to "n/a" if it is
        if representation.get('endTime') is None:
            representation['endTime'] = "n/a"
                
        return representation
        
        
