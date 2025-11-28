# mesh_app/urls.py
from django.urls import path
from .views import send_message, receive_messages

urlpatterns = [
    path('send/', send_message, name='send'),
    path('receive/', receive_messages, name='receive'),
]
