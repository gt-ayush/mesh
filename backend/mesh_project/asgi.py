import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import mesh_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mesh_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            mesh_app.routing.websocket_urlpatterns
        )
    ),
})
