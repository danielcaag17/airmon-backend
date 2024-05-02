from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'api/ws/chat/(?P<chat_id>\w+)/$', consumers.AsyncChatConsumer.as_asgi()),
]
