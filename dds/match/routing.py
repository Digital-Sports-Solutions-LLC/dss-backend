from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path("ws/match/<int:match_id>/", consumers.MatchConsumer.as_asgi())
]