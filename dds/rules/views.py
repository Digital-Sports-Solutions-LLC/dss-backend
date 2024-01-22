from django.shortcuts import render
from rest_framework import generics
from .models import RULES
from .serializers import RulesSerializer

class RulesListCreateView(generics.ListCreateAPIView):
    queryset = RULES.objects.all()
    serializer_class = RulesSerializer

class RulesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RULES.objects.all()
    serializer_class = RulesSerializer