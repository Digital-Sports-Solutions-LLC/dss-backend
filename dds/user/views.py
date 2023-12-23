from rest_framework import generics
from .models import USER
from .serializers import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = USER.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = USER.objects.all()
    serializer_class = UserSerializer