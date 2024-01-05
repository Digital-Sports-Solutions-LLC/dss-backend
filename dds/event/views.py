from rest_framework import generics
from django.shortcuts import render, redirect
from .forms import EventForm
from .models import EVENT
from .serializers import EventSerializer

def addEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.html')  #TODO FIX REDIRECT
    else:
        form = EventForm()

    return render(request, 'datatest.html', {'form': form})

class EventListCreateView(generics.ListCreateAPIView):
    queryset = EVENT.objects.all()
    serializer_class = EventSerializer

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EVENT.objects.all()
    serializer_class = EventSerializer

