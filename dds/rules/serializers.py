from rest_framework import serializers
from .models import RULES

class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RULES
        fields = '__all__'