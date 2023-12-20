from rest_framework import serializers
from .models import LEAGUE

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = LEAGUE
        fields = '__all__'