import os

from django.core.asgi import get_asgi_application

# Definição da configuração padrão do Django pelo arquivo settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vidaplus.settings')

application = get_asgi_application()
