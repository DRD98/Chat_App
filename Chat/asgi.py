import os
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

from ChatApp.routing import wsPattern


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chat.settings')

http_response_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": http_response_app,
    "websocket": URLRouter(wsPattern)
})
