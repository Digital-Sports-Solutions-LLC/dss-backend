from django.shortcuts import render
from rest_framework import generics
from .models import TEAM
from .serializers import TeamSerializer

class TeamListCreateView(generics.ListCreateAPIView):
    queryset = TEAM.objects.all()
    serializer_class = TeamSerializer

class TeamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TEAM.objects.all()
    serializer_class = TeamSerializer