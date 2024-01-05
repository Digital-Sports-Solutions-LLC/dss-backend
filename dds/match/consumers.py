import asyncio
import json
from channels.generic.websocket import WebsocketConsumer
from django.core.cache import cache
from django.utils.timezone import datetime

class MatchData():
    def __init__(self, match_id):
        self.match_id = match_id
        self.team1EndTime = datetime.now().isoformat()
        self.team1Paused = True
        self.team2EndTime = datetime.now().isoformat()
        self.team2Paused = True

    def __str__(self):
        return f"Match ID: {self.match_id}"

def get_data(match_id):
    data = cache.get("match" + str(match_id))
    if data is None:
        print("cache miss")
        data = MatchData(match_id).__dict__  # Use dictionary for better JSON representation
        cache.set("match" + str(match_id), data, 5 * 60)

    # Return JSON-formatted string
    return json.dumps(data)

def update_match(json_data):
    match_id = json_data["match_id"]

    # Retrieve existing MatchData instance from cache
    match_data = MatchData(match_id)
    cached_data = cache.get("match" + str(match_id))

    if cached_data:
        match_data.__dict__.update(cached_data)

    if json_data["side"] == "shotClock1":
        match_data.team1EndTime = json_data["endTime"]
        match_data.team1Paused = json_data["paused"]
    elif json_data["side"] == "shotClock2":
        match_data.team2EndTime = json_data["endTime"]
        match_data.team2Paused = json_data["paused"]

    cache.set("match" + str(match_id), match_data.__dict__, 5 * 60)

class MatchConsumer(WebsocketConsumer):
    def connect(self):
        # Extract match_id and side_id from the URL
        match_id = self.scope["url_route"]["kwargs"]["match_id"]
        self.accept()
        self.send(get_data(match_id))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        update_match(text_data_json)
        self.send(get_data(text_data_json["match_id"]))
