from django.db import models
from season.models import SEASON
from league.models import LEAGUE
from location.models import LOCATION
from event_type.models import EVENT_TYPE

class EVENT(models.Model):
    event_ID = models.AutoField(primary_key=True)
    season = models.ForeignKey(SEASON, on_delete=models.CASCADE)
    league = models.ForeignKey(LEAGUE, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.ForeignKey(LOCATION, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    event_type = models.ForeignKey(EVENT_TYPE, on_delete=models.CASCADE)
    graphic = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"