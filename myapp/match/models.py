from django.db import models
from django import forms
from team.models import Team

# Create your models here.
class Match(models.Model):
    matchid = models.AutoField(primary_key=True)
    event = models.CharField(max_length=100)
    team1 = models.ForeignKey('team.Team', on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey('team.Team', on_delete=models.CASCADE, related_name='team2')
    team1Score = models.PositiveIntegerField(default=0)
    team2Score = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.team1} vs {self.team2} @ {self.event}"
    
class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['team1', 'team2', 'team1Score', 'team2Score', 'event']


