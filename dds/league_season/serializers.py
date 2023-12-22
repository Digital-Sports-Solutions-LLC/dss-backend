from rest_framework import serializers
from .models import LEAGUE_SEASON
from league.serializers import LeagueSerializer
from season.serializers import SeasonSerializer
from team.serializers import TeamSerializer


class League_SeasonSerializer(serializers.ModelSerializer):
    league = LeagueSerializer()
    season = SeasonSerializer()
    champion = TeamSerializer()
    class Meta:
        model = LEAGUE_SEASON
        fields = '__all__'
        league = None
        season = None
        champion = None