from django.db import models
from django.core.validators import MaxValueValidator
from user.models import USER
from event.models import EVENT

class EVENT_ROSTER(models.Model):
    event_roster_ID = models.AutoField(primary_key=True)
    event = models.ForeignKey(EVENT, on_delete=models.CASCADE)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.event} - {self.user}"