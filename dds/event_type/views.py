from django.shortcuts import render
from rest_framework import generics
from .models import EVENT_TYPE
from .serializers import Event_TypeSerializer

class Event_TypeListCreateView(generics.ListCreateAPIView):
    queryset = EVENT_TYPE.objects.all()
    serializer_class = Event_TypeSerializer

class Event_TypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EVENT_TYPE.objects.all()
    serializer_class = Event_TypeSerializer