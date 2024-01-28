from django.db import models
from django.core.validators import MaxValueValidator
from point.models import POINT
from team.models import TEAM

class TIMEOUT(models.Model):
    timeout_ID = models.AutoField(primary_key=True)
    point = models.ForeignKey(POINT, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    takenBy = models.ForeignKey(TEAM, on_delete=models.CASCADE, null=True, blank=True)
    note = models.CharField(max_length=200)
    gameClockTime = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.point}"