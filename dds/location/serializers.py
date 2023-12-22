from rest_framework import serializers
from .models import LOCATION

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LOCATION
        fields = '__all__'
