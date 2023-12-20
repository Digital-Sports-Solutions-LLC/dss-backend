from django.shortcuts import render
from rest_framework import generics
from .models import LEAGUE
from .serializers import LeagueSerializer

class LeagueListCreateView(generics.ListCreateAPIView):
    queryset = LEAGUE.objects.all()
    serializer_class = LeagueSerializer

class LeagueRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LEAGUE.objects.all()
    serializer_class = LeagueSerializer
