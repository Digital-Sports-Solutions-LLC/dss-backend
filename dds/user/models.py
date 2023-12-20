from django.db import models
from django.core.validators import MaxValueValidator

class USER(models.Model):
    user_ID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.firstName}"