from django.db import models
from league.models import LEAGUE
from season.models import SEASON
from team.models import TEAM
from rules.models import RULES

# Create your models here.
class LEAGUE_SEASON(models.Model):
    league_Season_ID = models.AutoField(primary_key=True)
    league = models.ForeignKey(LEAGUE, on_delete=models.CASCADE)
    season = models.ForeignKey(SEASON, on_delete=models.CASCADE)
    rules = models.ForeignKey(RULES, on_delete=models.CASCADE)
    ruleBookLink = models.CharField(max_length=100)
    champion = models.ForeignKey(TEAM, on_delete=models.CASCADE, blank=True, null=True)
        
    def __str__(self):
        return f"{self.season} - {self.league}"