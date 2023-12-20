from django.db import models
from django.core.validators import MaxValueValidator

class LOCATION(models.Model):
    location_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    streetAddress = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"