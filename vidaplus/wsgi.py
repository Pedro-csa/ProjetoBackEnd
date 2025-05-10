import os

from django.core.wsgi import get_wsgi_application

# Definição da configuração padrão do Django pelo arquivo settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vidaplus.settings')

application = get_wsgi_application()
