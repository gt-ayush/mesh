# backend/mesh_project/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import mesh_app.routing_channels as mesh_routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mesh_project.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            mesh_routing.websocket_urlpatterns
        )
    ),
})
