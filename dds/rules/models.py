from django.db import models

# Create your models here.
class RULES(models.Model):
    rules_ID = models.AutoField(primary_key=True)
    minShotClock = models.IntegerField()
    maxShotClock = models.IntegerField(blank=True, null=True)
    numPlayers = models.IntegerField()
    maxToMinPlayers = models.IntegerField(blank=True, null=True)
    halfLength = models.IntegerField()
    runningClockDiff = models.IntegerField()
    halfTimeouts = models.IntegerField()
    otTimeouts = models.IntegerField()
        
    def __str__(self):
        return f"{self.rules_ID}: {self.minShotClock} sec - {self.halfLength} min"
