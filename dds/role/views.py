from django.shortcuts import render
from rest_framework import generics
from .models import ROLE
from .serializers import RoleSerializer

class RoleListCreateView(generics.ListCreateAPIView):
    queryset = ROLE.objects.all()
    serializer_class = RoleSerializer

class RoleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ROLE.objects.all()
    serializer_class = RoleSerializer