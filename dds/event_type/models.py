from django.db import models
from django.core.validators import MaxValueValidator

class EVENT_TYPE(models.Model):
    event_Type_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)   
    
    def __str__(self):
        return f"{self.title}"