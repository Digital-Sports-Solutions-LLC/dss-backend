from rest_framework import serializers
from .models import EVENT_ROSTER
from event.serializers import EventSerializer
#from user.serializers import UserSerializer


class Event_RosterSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    #user = UserSerializer()
    
    class Meta:
        model = EVENT_ROSTER
        fields = '__all__'
        event = None
        #user = None