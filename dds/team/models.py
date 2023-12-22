from django.db import models
from django.core.validators import MaxValueValidator
from league.models import LEAGUE
from location.models import LOCATION

class TEAM(models.Model):
    team_ID = models.AutoField(primary_key=True)
    teamName = models.CharField(max_length=100)
    teamAcronym = models.CharField(max_length=10)
    league = models.ForeignKey(LEAGUE, on_delete=models.CASCADE)
    location = models.ForeignKey(LOCATION, on_delete=models.CASCADE)
    yearFounded = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    graphic = models.ImageField(upload_to='images/', null=True, blank=True)
    active = models.BooleanField(default=True)
    yearDisbanded = models.PositiveIntegerField(validators=[MaxValueValidator(9999)], null=True, blank=True)
    
    def __str__(self):
        return f"{self.teamName}"