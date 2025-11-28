from django.urls import path
from .views import home, send_message, receive_messages

urlpatterns = [
    path("", home, name="home"),
    path("send/", send_message, name="send"),
    path("receive/", receive_messages, name="receive"),
]
