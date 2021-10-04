from django.urls import re_path

from . import consumers

ws_pattern = [
    re_path(r'ws/test/', consumers.ChatConsumer),
]
