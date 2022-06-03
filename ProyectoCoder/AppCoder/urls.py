
from django.urls import path
#from django.urls import views
from AppCoder.views import inicio, cursos, profesores, entregables, estudiantes, cursoFormulario, profesorFormulario,busquedaCamada
from AppCoder.views import buscar



urlpatterns = [
    path('Inicio', inicio, name= 'Inicio'),
    path('Cursos/',cursos, name='Cursos'),
    path('Profesores/',profesores, name='Profesores'),
    path('Estudiantes/',estudiantes, name='Estudiantes'),
    path('Entregables/',entregables, name='Entregables'),
    path('cursoFormulario/', cursoFormulario, name= 'cursoFormulario'),
    path('profesorFormulario', profesorFormulario, name= 'profesorFormulario'),
    path('busquedaCamada', busquedaCamada, name= 'busquedaCamada'),
    path('buscar',buscar, name='buscar'),
        
]