from django.db import models
from django.core.validators import MaxValueValidator

class MATCH_TYPE(models.Model):
    match_type_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.title}"
