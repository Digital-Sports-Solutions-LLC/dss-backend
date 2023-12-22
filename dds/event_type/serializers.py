from rest_framework import serializers
from .models import EVENT_TYPE

class Event_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EVENT_TYPE
        fields = '__all__'