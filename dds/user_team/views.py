from rest_framework import generics
from .models import USER_TEAM
from .serializers import User_TeamSerializer

class User_TeamListCreateView(generics.ListCreateAPIView):
    queryset = USER_TEAM.objects.all()
    serializer_class = User_TeamSerializer

class User_TeamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = USER_TEAM.objects.all()
    serializer_class = User_TeamSerializer