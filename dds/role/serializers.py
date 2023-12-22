from rest_framework import serializers
from .models import ROLE

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ROLE
        fields = '__all__'
