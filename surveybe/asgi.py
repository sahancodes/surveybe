"""
ASGI config for surveybe project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# import notifications.routing

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'surveybe.settings')

# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             notifications.routing.websocket_urlpatterns
#         )
#     ),
#     'http': get_asgi_application(),
# })

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import notifications.routing as router

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'surveybe.settings')

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            router.websocket_urlpatterns
        )
    ),
    'http': get_asgi_application(),
})