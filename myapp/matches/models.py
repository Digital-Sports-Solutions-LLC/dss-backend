from django.db import models

# Create your models here.
class Match(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    team1Score = models.IntegerField()
    team2Score = models.IntegerField()
    tournament = models.CharField(max_length=100)
    court = models.IntegerField()
    datetime = models.DateTimeField()
    status = models.CharField(max_length=100)    
    livestreamLink = models.CharField(max_length=300, null=True, blank=True)
    refereeCode = models.IntegerField()
    style = models.CharField(max_length=100)
    
    def __str__(self):
        return self.team1 + ' vs ' + self.team2 + ' @ ' + self.tournament