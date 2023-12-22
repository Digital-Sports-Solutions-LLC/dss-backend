from django.shortcuts import render
from rest_framework import generics
from .models import COURT
from .serializers import CourtSerializer

class CourtListCreateView(generics.ListCreateAPIView):
    queryset = COURT.objects.all()
    serializer_class = CourtSerializer

class CourtRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = COURT.objects.all()
    serializer_class = CourtSerializer