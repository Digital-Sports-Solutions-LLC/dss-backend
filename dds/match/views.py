from django.shortcuts import render
from rest_framework import generics
from .models import MATCH
from point.models import POINT
from timeout.models import TIMEOUT
from .serializers import MatchSerializer
from .consumers import get_data
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class MatchListCreateView(generics.ListCreateAPIView):
    queryset = MATCH.objects.all()
    serializer_class = MatchSerializer

class MatchRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MATCH.objects.all()
    serializer_class = MatchSerializer
    
def getScore(team_ID, match_ID):
    points = POINT.objects.filter(winner=team_ID, match=match_ID)
    return len(points)

def getPointIDsInHalf(match_ID, half):
    points = POINT.objects.filter(match=match_ID, half=half)
    point_ids = [point.point_ID for point in points]
    return point_ids

def getTimeouts(team_ID, point_ID, half): 
    num = 0       
    for point in point_ID:
        timeouts = TIMEOUT.objects.filter(takenBy=team_ID, point=point)
        num += len(timeouts)
          
    if (half == "OT"):
        return 1 - num
    else:
        return 2 - num
                
def index(request):
    
    matches = MATCH.objects.all().order_by('-court_event__event__startDate')[:20]
    
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
        
    return render(request, "home.html", context)

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
    
    return render(request, "jobSelection.html", context)

def shotClocker(request, pk, num):
    match = MATCH.objects.get(match_ID=pk)
    data = get_data(pk)
    
    context = {
        "matchId": match.match_ID,
        "num": num,
    }
    
    if num == 1:
        context["team"] = match.team1.teamAcronym
        context["endTime"] = data["team1EndTime"]
        context["timePaused"] = data["team1TimePaused"]
        context["undoTime"] = data["team1UndoTime"]
        context["paused"] = data["team1Paused"]
        context["countDuration"] = data["team1CountDuration"]
    elif num == 2:
        context["team"] = match.team2.teamAcronym
        context["endTime"] = data["team2EndTime"]
        context["timePaused"] = data["team2TimePaused"]
        context["undoTime"] = data["team2UndoTime"]
        context["paused"] = data["team2Paused"]
        context["countDuration"] = data["team2CountDuration"]
    
    return render(request, "shotClocker.html", context)

def referee(request, pk):
    match = MATCH.objects.get(match_ID=pk)
    data = get_data(pk)
    
    context = {
        "matchId": match.match_ID,
        "team1": match.team1.teamAcronym,
        "team1Score": getScore(match.team1.team_ID, match.match_ID),
        "team2": match.team2.teamAcronym,  
        "team2Score": getScore(match.team2.team_ID, match.match_ID),        
    }
    
    context["endTime"] = data["halfEndTime"]
    context["timePaused"] = data["timePaused"]
    context["timeoutEndTime"] = data["timeoutEndTime"]
    context["paused"] = data["paused"]
    context["middleOfPoint"] = data["middleOfPoint"]
    context["activeTimeout"] = data["activeTimeout"]
    context["half"] = data["half"]
    
    vals = getPointIDsInHalf(match.match_ID, data["half"])
        
    context["team1Timeouts"] = getTimeouts(match.team1.team_ID, vals, data["half"])
    context["team2Timeouts"] = getTimeouts(match.team2.team_ID, vals, data["half"])
    
    return render(request, "gameClocker.html", context)

def update(request):
    # TODO: Update database with new data
    if request.method == "POST":
        try:
            request = request.POST["request"]
            if request == "startpoint":
                match = request.POST["matchId"]
                half = request.POST["half"]
                startTime = request.POST["startTime"]
                pointNumber = 
                
                newPoint = POINT(match=match, pointNumber=1, half=half, startTime=startTime)                
                               
            elif request == "endpoint":
           
           
           
           return JsonResponse({"success": "Match updated successfully."}, status=201)
       
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": 'Invalid request method'}, status=400)
    
