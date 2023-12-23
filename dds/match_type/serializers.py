from rest_framework import serializers
from .models import MATCH_TYPE

class Match_TypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MATCH_TYPE
        fields = '__all__'