from django.db import models

# Create your models here.
class University(models.Model):
    universityid = models.AutoField(primary_key=True)
    universityName = models.CharField(max_length=100)
    universityAcronym = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.universityName