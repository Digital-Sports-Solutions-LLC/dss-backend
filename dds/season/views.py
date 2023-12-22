from django.shortcuts import rendergenerics
from rest_framework import generics
from .models import SEASON
from .serializers import SeasonSerializer

class SeasonListCreateView(generics.ListCreateAPIView):
    queryset = SEASON.objects.all()
    serializer_class = SeasonSerializer

class SeasonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SEASON.objects.all()
    serializer_class = SeasonSerializer