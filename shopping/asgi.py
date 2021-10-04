# # mysite/asgi.py
# import os

# from channels.routing import ProtocolTypeRouter,URLRouter
# from django.core.asgi import get_asgi_application 
# from home.routing import *
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping.settings')
# application = get_asgi_application()


# application = ProtocolTypeRouter({
#     "websocket":URLRouter(ws_pattern),
# })