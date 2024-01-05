from django.shortcuts import render
from rest_framework import generics
from .models import MATCH
from point.models import POINT
from .serializers import MatchSerializer
from .consumers import get_data

class MatchListCreateView(generics.ListCreateAPIView):
    queryset = MATCH.objects.all()
    serializer_class = MatchSerializer

class MatchRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MATCH.objects.all()
    serializer_class = MatchSerializer
    
def getScore(team_ID, match_ID):
    points = POINT.objects.filter(winner=team_ID, match=match_ID)
    return len(points) 
    
def index(request):
    
    matches = MATCH.objects.all().order_by('-court_event__event__startDate')[:7]
    
    ret = []
    num = 0
    
    for match in matches:
        ret.append({
            "matchID": match.match_ID,
            "event": match.court_event.event.name,
            "courtNumber": match.court_event.courtNumber,
            "status": match.status,
            "startTime": match.startTime,
            "startDate": match.court_event.event.startDate,
            "team1": match.team1.teamAcronym,
            "team1Score": getScore(match.team1.team_ID, match.match_ID),
            "team2": match.team2.teamAcronym,
            "team2Score": getScore(match.team2.team_ID, match.match_ID),
        })
        
        num = num + 1
        
    context = {
        "num_matches": num,
        "matches": ret,
    }
        
    return render(request, "landing.html", context)

def match(request, pk):
    match = MATCH.objects.get(match_ID=pk)
    context = {
        "matchID": match.match_ID,
        "event": match.court_event.event.name,
        "courtNumber": match.court_event.courtNumber,
        "status": match.status,
        "team1": match.team1.teamAcronym,
        "team1Score": getScore(match.team1.team_ID, match.match_ID),
        "team2": match.team2.teamAcronym,        
        "team2Score": getScore(match.team2.team_ID, match.match_ID),
    }
    
    return render(request, "match.html", context)

def shotClocker(request, pk, num):
    match = MATCH.objects.get(match_ID=pk)
    data = get_data(pk)
    
    context = {
        "matchID": match.match_ID,
        "event": match.court_event.event.name,
        "courtNumber": match.court_event.courtNumber,
        "status": match.status,
        "num": num,
    }
    
    if num == 1:
        context["team"] = match.team1.teamAcronym
        context["teamScore"] = getScore(match.team1.team_ID, match.match_ID)
        context["teamEndTime"] = data[1]
    elif num == 2:
        context["team"] = match.team2.teamAcronym
        context["teamScore"] = getScore(match.team2.team_ID, match.match_ID)
        context["teamEndTime"] = data[3]
    
    return render(request, "shotClocker.html", context)

def referee(request, pk):
    match = MATCH.objects.get(match_ID=pk)
    context = {
        "matchID": match.match_ID,
        "event": match.court_event.event.name,
        "courtNumber": match.court_event.courtNumber,
        "status": match.status,
        "team1": match.team1.teamAcronym,
        "team1Score": getScore(match.team1.team_ID, match.match_ID),
        "team2": match.team2.teamAcronym,        
        "team2Score": getScore(match.team2.team_ID, match.match_ID),
    }
    
    return render(request, "referee.html", context)
