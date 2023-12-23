from rest_framework import serializers
from .models import USER_TEAM
from user.serializers import UserSerializer
from team.serializers import TeamSerializer
from role.serializers import RoleSerializer
from season.serializers import SeasonSerializer

class User_TeamSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    team = TeamSerializer()
    role = RoleSerializer()
    season = SeasonSerializer()
    
    class Meta:
        model = USER_TEAM
        fields = '__all__'
        user = None
        team = None
        role = None
        season = None
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Check if 'graphic' is None and set it to a default value if it is
        if representation['graphic'] is None:
            request = self.context.get('request')
            if request is not None:
                domain = request.get_host()
                representation['graphic'] = f"http://{domain}/media/images/file-not-found.jpg"
    
        return representation