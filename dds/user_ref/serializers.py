from rest_framework import serializers
from .models import USER_REF
from user.serializers import UserSerializer
from league.serializers import LeagueSerializer


class User_RefSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    league = LeagueSerializer()
    
    class Meta:
        model = USER_REF
        fields = '__all__'
        user = None
        league = None