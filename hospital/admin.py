from django.contrib import admin
from .models import *

# Registra os modelos para que apareçam na tela administrativa
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Consulta)
