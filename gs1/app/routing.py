from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sc/', consumers.MySyncConsumer.as_asgi()),  # Replace 'somepath' with your desired path
    path('ws/ac/', consumers.MyAsyncConsumer.as_asgi()),  # Replace 'somepath' with your desired path
]

