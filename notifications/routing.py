from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/notifications/$', consumers.NotificationsConsumer.as_asgi()),
    # Add other WebSocket routes if needed
]