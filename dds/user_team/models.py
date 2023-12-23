from django.db import models
from django.core.validators import MaxValueValidator
from user.models import USER
from team.models import TEAM
from role.models import ROLE
from season.models import SEASON

class USER_TEAM(models.Model):
    user_team_ID = models.AutoField(primary_key=True)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    team = models.ForeignKey(TEAM, on_delete=models.CASCADE)
    role = models.ForeignKey(ROLE, on_delete=models.CASCADE)
    season = models.ForeignKey(SEASON, on_delete=models.CASCADE)
    number = models.PositiveBigIntegerField()
    captain = models.BooleanField(default=True)
    graphic = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.team} - {self.season}"