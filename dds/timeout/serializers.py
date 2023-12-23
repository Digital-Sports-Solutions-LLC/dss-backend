from rest_framework import serializers
from .models import TIMEOUT
from point.serializers import PointSerializer
from team.serializers import TeamSerializer

class TimeoutSerializer(serializers.ModelSerializer):
    point = PointSerializer()
    takenBy = TeamSerializer()
    
    class Meta:
        model = TIMEOUT
        fields = '__all__'
        point = None
        takenBy = None
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
                
        # Check if 'takenBy' is None and set it to "n/a" if it is
        if representation.get('takenBy') is None:
            representation['takenBy'] = "n/a"
                
        return representation