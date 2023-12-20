from django.db import models
from django.core.validators import MaxValueValidator
from court.models import COURT
from match_type.models import MATCH_TYPE
from team.models import TEAM
from user_ref.models import USER_REF

class MATCH(models.Model):
    match_ID = models.AutoField(primary_key=True)
    court_event = models.ForeignKey(COURT, on_delete=models.CASCADE)
    match_type = models.ForeignKey(MATCH_TYPE, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    startTime = models.TimeField()
    endTime = models.TimeField()
    team1 = models.ForeignKey(TEAM, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(TEAM, on_delete=models.CASCADE, related_name='team2')
    headRef = models.ForeignKey(USER_REF, on_delete=models.CASCADE)
    officiatingTeam = models.ForeignKey(TEAM, on_delete=models.CASCADE, related_name='officiatingTeam')
    
    def __str__(self):
        return f"Court: {self.court_event.courtNumber} - Event: {self.court_event.event.name} - Team 1: {self.team1} vs. Team 2: {self.team2}"