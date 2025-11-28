
from django.http import JsonResponse
from .routing import send_message, receive_messages
from django.shortcuts import render
def send_view(request):
    msg = request.GET.get('msg', '')
    if msg:
        send_message(msg)
        return JsonResponse({'status': 'success', 'message': msg})
    return JsonResponse({'status': 'error', 'message': 'No message provided'})

def receive_view(request):
    messages = receive_messages()
    return JsonResponse({'messages': messages})

def home(request):
    return render(request, "index.html")
