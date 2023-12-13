from django.db import models
from django.core.validators import MaxValueValidator
from team.models import Team

# Create your models here.
class Season(models.Model):
    seasonid = models.AutoField(primary_key=True)
    seasonYear = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    champion = models.ForeignKey('team.Team', on_delete=models.CASCADE, related_name='champion', null=True, blank=True)
    
    def __str__(self):
        return str(self.seasonYear)

class SeasonTeam(models.Model):
    seasonTeamid = models.AutoField(primary_key=True)
    season = models.ForeignKey('season.Season', on_delete=models.CASCADE)
    team = models.ForeignKey('team.Team', on_delete=models.CASCADE)
    teamActive = models.BooleanField(default=True)
        
    def __str__(self):
        return f"{self.season.seasonYear} - {self.team.teamName}"