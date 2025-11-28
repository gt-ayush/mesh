# mesh_app/views.py
from django.http import JsonResponse
from .store import messages_store  # import from store instead
from django.shortcuts import render

def send_message(request):
    msg = request.GET.get('msg', '')
    if msg:
        messages_store.append(msg)
        return JsonResponse({"status": "success", "message": msg})
    return JsonResponse({"status": "fail", "message": "No message provided"})

def receive_messages(request):
    return JsonResponse({"messages": messages_store})
def home(request):
    return render(request, 'index.html')
