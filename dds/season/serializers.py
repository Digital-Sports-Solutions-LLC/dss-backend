from rest_framework import serializers
from .models import SEASON

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEASON
        fields = '__all__'