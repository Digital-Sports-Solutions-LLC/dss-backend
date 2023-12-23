from rest_framework import generics
from .models import POINT
from .serializers import PointSerializer

class PointListCreateView(generics.ListCreateAPIView):
    queryset = POINT.objects.all()
    serializer_class = PointSerializer

class PointRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = POINT.objects.all()
    serializer_class = PointSerializer