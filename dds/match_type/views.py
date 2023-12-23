from rest_framework import generics
from .models import MATCH_TYPE
from .serializers import Match_TypeSerializer

class Match_TypeListCreateView(generics.ListCreateAPIView):
    queryset = MATCH_TYPE.objects.all()
    serializer_class = Match_TypeSerializer

class Match_TypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MATCH_TYPE.objects.all()
    serializer_class = Match_TypeSerializer