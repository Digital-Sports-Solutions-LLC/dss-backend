from rest_framework import generics
from .models import EVENT_ROSTER
from .serializers import Event_RosterSerializer

class Event_RosterListCreateView(generics.ListCreateAPIView):
    queryset = EVENT_ROSTER.objects.all()
    serializer_class = Event_RosterSerializer

class Event_RosterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EVENT_ROSTER.objects.all()
    serializer_class = Event_RosterSerializer