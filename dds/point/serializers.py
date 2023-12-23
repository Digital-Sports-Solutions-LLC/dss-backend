from rest_framework import serializers
from .models import POINT
from match.serializers import MatchSerializer
from team.serializers import TeamSerializer

class PointSerializer(serializers.ModelSerializer):
    match = MatchSerializer()
    winner = TeamSerializer()
    
    class Meta:
        model = POINT
        fields = '__all__'
        match = None
        winner = None
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
                
        # Check if 'endTime' is None and set it to "n/a" if it is
        if representation.get('endTime') is None:
            representation['endTime'] = "n/a"
            
        # Check if 'winner' is None and set it to "n/a" if it is
        if representation.get('winner') is None:
            representation['winner'] = "n/a"
            
        # Check if 'note' is None and set it to "n/a" if it is
        if representation.get('note') is None:
            representation['note'] = "n/a"
                
        return representation