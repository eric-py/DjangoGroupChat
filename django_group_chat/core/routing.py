from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

from chat.routing import websocket_urlpatterns

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        SessionMiddlewareStack(
            AuthMiddlewareStack(
                URLRouter(
                    websocket_urlpatterns
                )
            )
        )
    ),
})