from point.models import POINT
from league_season.models import LEAGUE_SEASON
from rules.models import RULES
from timeout.models import TIMEOUT

def getScore(team_ID, match_ID):
    points = POINT.objects.filter(winner=team_ID, match=match_ID)
    return len(points)

def getPointIDsInHalf(match_ID, half):
    points = POINT.objects.filter(match=match_ID, half=half)
    point_ids = [point.point_ID for point in points]
    return point_ids

def getRules(season_ID, league_ID):
    rules_ID = LEAGUE_SEASON.objects.get(season=season_ID, league=league_ID).rules.rules_ID
    rules = RULES.objects.get(rules_ID=rules_ID)
    return rules

def getTimeouts(team_ID, point_ID, half, rules): 
    num = 0       
    for point in point_ID:
        timeouts = TIMEOUT.objects.filter(takenBy=team_ID, point=point)
        num += len(timeouts)
          
    if (half == "OT"):
        return rules.otTimeouts - num
    else:
        return rules.halfTimeouts - num