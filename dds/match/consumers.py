from datetime import timedelta
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.cache import cache
from django.utils.timezone import datetime
from channels.db import database_sync_to_async

cacheLength = 5 * 60 * 60 # 5 hours

class MatchData():
    def __init__(self, match_id):
        self.match_id = match_id
        self.team1EndTime = datetime.now().isoformat()
        self.team1TimePaused = datetime.now().isoformat()
        self.team1UndoTime = datetime.now().isoformat()
        self.team1Paused = True
        self.team1CountDuration = "minimum"
        self.team2EndTime = datetime.now().isoformat()
        self.team2TimePaused = datetime.now().isoformat()
        self.team2UndoTime = datetime.now().isoformat()
        self.team2Paused = True
        self.team2CountDuration = "minimum"
        self.halfEndTime = (datetime.now() + timedelta(minutes=25)).isoformat()
        self.timePaused = datetime.now().isoformat()
        self.timeoutEndTime = datetime.now().isoformat()
        self.paused = True
        self.middleOfPoint = False
        self.activeTimeout = False
        self.half = "1st"      
        

    def __str__(self):
        return f"Match ID: {self.match_id}"


def get_data(match_id):
    data = cache.get("match" + str(match_id))
    
    if data is None:
        print("cache miss")
        data = MatchData(match_id).__dict__  # Use dictionary for better JSON representation
        cache.set("match" + str(match_id), data, cacheLength)

    # Return JSON-formatted string
    return data


async def async_update_match(json_data):
    match_id = json_data["match_id"]

    # Retrieve existing MatchData instance from cache
    data = MatchData("match" + str(match_id))

    if json_data["side"] == "shotClock1":
        data.team1EndTime = json_data["endTime"]
        data.team1TimePaused = json_data["timePaused"]
        data.team1UndoTime = json_data["undoTime"]
        data.team1Paused = json_data["paused"]
        data.team1CountDuration = json_data["countDuration"]
    elif json_data["side"] == "shotClock2":
        data.team2EndTime = json_data["endTime"]
        data.team2TimePaused = json_data["timePaused"]
        data.team2UndoTime = json_data["undoTime"]
        data.team2Paused = json_data["paused"]
        data.team2CountDuration = json_data["countDuration"]
    elif json_data["side"] == "gameClock":
        data.halfEndTime = json_data["endTime"]
        data.timePaused = json_data["timePaused"]
        data.timeoutEndTime = json_data["timeoutEndTime"]
        data.paused = json_data["paused"]
        data.middleOfPoint = json_data["middleOfPoint"]
        data.activeTimeout = json_data["activeTimeout"]
        data.half = json_data["half"]
        

    await database_sync_to_async(cache.set)("match" + str(match_id), data.__dict__, cacheLength)


class MatchConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract match_id from the URL
        match_id = self.scope["url_route"]["kwargs"]["match_id"]
        self.room_group_name = f"match{match_id}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Send initial data to the client
        #await self.send(get_data(match_id))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        await async_update_match(text_data_json)

        # Broadcast to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_data_to_group',
                'message': json.dumps(get_data(text_data_json["match_id"]))
            }
        )

    # Receive message from room group
    async def send_data_to_group(self, event):
        # Send message to WebSocket
        await self.send(event['message'])
