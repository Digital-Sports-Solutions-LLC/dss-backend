from django.shortcuts import render
from rest_framework import generics
from .models import MATCH
from .serializers import MatchSerializer

class MatchListCreateView(generics.ListCreateAPIView):
    queryset = MATCH.objects.all()
    serializer_class = MatchSerializer

class MatchRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MATCH.objects.all()
    serializer_class = MatchSerializer
    
def index(request):
    matches = MATCH.objects.all()
    
    ret = []
    num = 0
    
    for match in matches:
        ret.append({
            "match_ID": match.match_ID,
            "event": match.court_event.event.name,
            "court_number": match.court_event.courtNumber,
            "status": match.status,
            "startTime": match.startTime,
            "team1": match.team1.teamAcronym,
            "team2": match.team2.teamAcronym,
        })
        
        num = num + 1
        
    context = {
        "num_matches": num,
        "matches": ret,
    }
    
    return render(request, "landing.html", context)
