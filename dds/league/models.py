from django.db import models
from django.core.validators import MaxValueValidator

class LEAGUE(models.Model):
    league_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=10)
    yearFounded = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    graphic = models.ImageField(upload_to='images/', null=True, blank=True)
    altGraphic = models.ImageField(upload_to='images/', null=True, blank=True)
        
    def __str__(self):
        return f"{self.name}"