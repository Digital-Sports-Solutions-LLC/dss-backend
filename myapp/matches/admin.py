from django.contrib import admin
from .models import Match

# Register your models here.

class MemeberAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2', 'team1Score', 'team2Score', 'tournament', 'court', 'datetime', 'status', 'livestreamLink', 'refereeCode', 'style')

admin.site.register(Match, MemeberAdmin)