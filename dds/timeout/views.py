from rest_framework import generics
from .models import TIMEOUT
from .serializers import TimeoutSerializer

class TimeoutListCreateView(generics.ListCreateAPIView):
    queryset = TIMEOUT.objects.all()
    serializer_class = TimeoutSerializer

class TimeoutRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TIMEOUT.objects.all()
    serializer_class = TimeoutSerializer