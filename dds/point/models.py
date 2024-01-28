from django.db import models
from django.core.validators import MaxValueValidator
from match.models import MATCH
from team.models import TEAM

class POINT(models.Model):
    point_ID = models.AutoField(primary_key=True)
    match = models.ForeignKey(MATCH, on_delete=models.CASCADE)
    pointNumber = models.PositiveIntegerField()
    half = models.CharField(max_length=100)
    startTime = models.TimeField()
    endTime = models.TimeField(blank=True, null=True)
    winner = models.ForeignKey(TEAM, on_delete=models.CASCADE, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    gameClockStart = models.CharField(max_length=100, blank=True, null=True)
    gameClockEnd = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"Point #: {self.pointNumber} - {self.match}"