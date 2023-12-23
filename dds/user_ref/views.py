from rest_framework import generics
from .models import USER_REF
from .serializers import User_RefSerializer

class User_RefListCreateView(generics.ListCreateAPIView):
    queryset = USER_REF.objects.all()
    serializer_class = User_RefSerializer

class User_RefRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = USER_REF.objects.all()
    serializer_class = User_RefSerializer