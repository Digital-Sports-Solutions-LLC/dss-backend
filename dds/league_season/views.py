from django.shortcuts import render
from rest_framework import generics
from .models import LEAGUE_SEASON
from .serializers import League_SeasonSerializer

class League_SeasonListCreateView(generics.ListCreateAPIView):
    queryset = LEAGUE_SEASON.objects.all()
    serializer_class = League_SeasonSerializer

class League_SeasonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LEAGUE_SEASON.objects.all()
    serializer_class = League_SeasonSerializer