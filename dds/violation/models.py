from django.db import models
from court.models import COURT
from django.core.validators import MaxValueValidator

class Violation(models.Model):
    violation_ID = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    team = models.ForeignKey(TEAM, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.firstName}"