from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_view, name='send'),
    path('receive/', views.receive_view, name='receive'),
]
