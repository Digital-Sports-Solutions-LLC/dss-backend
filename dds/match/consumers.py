import json
from channels.generic.websocket import WebsocketConsumer
from django.core.cache import cache

class MatchData():
    def __init__(self, match_id, team1EndTime, team2EndTime):
        self.match_id = match_id
        self.team1EndTime = team1EndTime
        self.team2EndTime = team2EndTime

    def __str__(self):
        return f"Match ID: {self.match_id} - Data: {self.data}"
    
def get_data(match_id):
    data = cache.get("match"+str(match_id))
    if data is None:
        data = list(MatchData(match_id, 0, 0).__dict__.values())
        cache.set("match"+str(match_id), data, 5*60)
    return data

class MatchConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()        
        self.send(text_data=json.dumps({"message": get_data(1)}))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))