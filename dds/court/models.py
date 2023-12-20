from django.db import models
from django.core.validators import MaxValueValidator
from event.models import EVENT

class COURT(models.Model):
    court_ID = models.AutoField(primary_key=True)
    event = models.ForeignKey(EVENT, on_delete=models.CASCADE)
    courtNumber = models.PositiveIntegerField()
    livestreamed = models.BooleanField(default=False)
    link = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.courtNumber} - {self.event}"