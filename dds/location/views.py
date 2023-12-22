from django.shortcuts import render
from rest_framework import generics
from .models import LOCATION
from .serializers import LocationSerializer

class LocationListCreateView(generics.ListCreateAPIView):
    queryset = LOCATION.objects.all()
    serializer_class = LocationSerializer

class LocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LOCATION.objects.all()
    serializer_class = LocationSerializer