from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class SEASON(models.Model):
    season_ID = models.AutoField(primary_key=True)
    year = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    
    def __str__(self):
        return f"{self.year}"
