from rest_framework import serializers
from .models import MATCH
from court.serializers import CourtSerializer
from match_type.serializers import Match_TypeSerializer
from team.serializers import TeamSerializer
from user_ref.serializers import User_RefSerializer
from .utils import getScore, getPointIDsInHalf, getRules, getTimeouts

class MatchSerializer(serializers.ModelSerializer):
    court_event = CourtSerializer()
    match_type = Match_TypeSerializer()
    team1 = TeamSerializer()
    team2 = TeamSerializer()
    headRef = User_RefSerializer()
    officiatingTeam = TeamSerializer()

    class Meta:
        model = MATCH
        fields = '__all__'
        court_event = None
        match_type = None
        team1 = None
        team2 = None
        headRef = None
        officiatingTeam = None
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        match_id = instance.match_ID
        rules = getRules(instance.court_event.event.season, instance.court_event.event.league)
        team1Score = getScore(instance.team1.team_ID, match_id)
        team2Score = getScore(instance.team2.team_ID, match_id)
        
        representation['team1Score'] = team1Score
        representation['team2Score'] = team2Score
        
        first_vals = getPointIDsInHalf(match_id, "1st")
        representation["team1TOL1st"] = getTimeouts(instance.team1.team_ID, first_vals, "1st", rules)
        representation["team2TOL1st"] = getTimeouts(instance.team2.team_ID, first_vals, "1st", rules)

        second_vals = getPointIDsInHalf(match_id, "2nd")
        representation["team1TOL2nd"] = getTimeouts(instance.team1.team_ID, second_vals, "2nd", rules)
        representation["team2TOL2nd"] = getTimeouts(instance.team2.team_ID, second_vals, "2nd", rules)

        ot_vals = getPointIDsInHalf(match_id, "OT")
        representation["team1TOLOT"] = getTimeouts(instance.team1.team_ID, ot_vals, "OT", rules)
        representation["team2TOLOT"] = getTimeouts(instance.team2.team_ID, ot_vals, "OT", rules)


        # Check if 'endTime' is None and set it to "n/a" if it is
        if representation.get('endTime') is None:
            representation['endTime'] = "n/a"
                
        return representation
        
        
