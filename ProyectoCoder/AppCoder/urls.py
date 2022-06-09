
from django.urls import path
#from django.urls import views
from AppCoder.views import inicio, cursos, profesores, entregables, estudiantes, cursoFormulario, profesorFormulario,busquedaCamada
from AppCoder.views import buscar, leerProfesores, leerCurso, eliminarCurso, editarCurso, Estudianteslist, EstudianteDetalle, EstudianteCreacion, EstudianteEliminacion, EstudianteEdicion



urlpatterns = [
    path('Inicio', inicio, name= 'Inicio'),
    #path('Cursos/',cursos, name='Cursos'),
    #path('Profesores/',profesores, name='Profesores'),
    path('Estudiantes/',estudiantes, name='Estudiantes'),
    path('Entregables/',entregables, name='Entregables'),
    path('cursoFormulario/', cursoFormulario, name= 'cursoFormulario'),
    path('profesorFormulario', profesorFormulario, name= 'profesorFormulario'),
    path('busquedaCamada', busquedaCamada, name= 'busquedaCamada'),
    path('buscar',buscar, name='buscar'),
    path('profesores/', leerProfesores, name= 'Profesores'),
    path('Cursos/', leerCurso, name= 'Cursos'),
    path('eliminarCurso/<camada>', eliminarCurso, name= 'eliminarCurso'),
    path('editarCurso/<curso_camada>', editarCurso, name= 'editarCurso'),  
    #-------------------------------------------------------------------
    path('estudiante/list/', Estudianteslist.as_view(), name='estudiante_listar'),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='estudiante_crear'),
    path('estudiante/edicion/<pk>', EstudianteEdicion.as_view(), name='estudiante_editar'),
    path('estudiante/borrar/<pk>', EstudianteEliminacion.as_view(), name='estudiante_borrar'),   
]