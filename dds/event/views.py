from rest_framework import generics
from .models import EVENT
from .serializers import EventSerializer

class EventListCreateView(generics.ListCreateAPIView):
    queryset = EVENT.objects.all()
    serializer_class = EventSerializer

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EVENT.objects.all()
    serializer_class = EventSerializer