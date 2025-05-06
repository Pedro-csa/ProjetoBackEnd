from django.contrib import admin
from django.urls import path, include
from hospital.views import *

urlpatterns = [
    #Bloco início
    path('',Index,name='index'),
    path('login/', adminlogin, name='login'),
    path('admin/', admin.site.urls),
    path('admin_home/', home, name='admin_home'),
    path('sobre/', Sobre, name="sobre"),
    path('contato/', contato, name='contato'),
    path('logout', Logout, name='logout'),

    #Bloco do Médico    
    path('add_medico', add_medico, name='add_medico'),
    path('view_medico', view_medico, name='view_medico'),
    path('edit_medico/<int:pid>',edit_medico,name='edit_medico'),
    path('delete_medico/<int:pid>', Delete_medico, name='delete_medico'),

    #Bloco do Paciente
    path('add_paciente', add_paciente, name='add_paciente'),
    path('view_paciente', view_paciente, name='view_paciente'),
    path('delete_paciente/<int:pid>', Delete_Paciente, name='delete_paciente'),
    path('edit_paciente/<int:pid>',edit_paciente,name='edit_paciente'),

    #Bloco da Consulta
    path('add_consulta', add_consulta, name='add_consulta'),
    path('view_consulta', view_consulta, name='view_consulta'),
    path('delete_consulta/<int:pid>', delete_consulta, name='delete_consulta')
    
    
]