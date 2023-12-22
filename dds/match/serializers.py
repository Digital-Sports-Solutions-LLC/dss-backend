# from rest_framework import serializers
# from .models import MATCH
# from court.serializers import CourtSerializer
# from match_type.serializers import MatchTypeSerializer
# from team.serializers import TeamSerializer
# from user_ref.serializers import UserRefSerializer

# class MatchSerializer(serializers.ModelSerializer):
#     court_event = CourtSerializer()
#     match_type = MatchTypeSerializer()
#     team1 = TeamSerializer()
#     team2 = TeamSerializer()
#     headRef = UserRefSerializer()
#     officiatingTeam = TeamSerializer()

#     class Meta:
#         model = MATCH
#         exclude = ('court_event', 'match_type', 'team1', 'team2', 'headRef', 'officiatingTeam')

# # Assuming you have serializers for COURT, MATCH_TYPE, TEAM, and USER_REF models
# # If not, you should create serializers for those models similarly to the MatchSerializer
