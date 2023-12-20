from django.db import models
from django.core.validators import MaxValueValidator
from user.models import USER
from league.models import LEAGUE

class USER_REF(models.Model):
    user_ref_ID = models.AutoField(primary_key=True)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    league = models.ForeignKey(LEAGUE, on_delete=models.CASCADE)
    canRef = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user} - Can Ref?: {self.canRef}"