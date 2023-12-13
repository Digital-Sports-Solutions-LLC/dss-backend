from django.db import models
from django.core.validators import MaxValueValidator
from university.models import University

# Create your models here.   
class Team(models.Model):
    teamid = models.AutoField(primary_key=True)
    teamName = models.CharField(max_length=100)
    teamAcronym = models.CharField(max_length=10)
    university = models.ForeignKey('university.University', on_delete=models.CASCADE)
    yearFounded = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    yearDisbanded = models.PositiveIntegerField(validators=[MaxValueValidator(9999)], null=True, blank=True)
    active = models.BooleanField(default=True)     
    
    def __str__(self):
        return self.teamName 