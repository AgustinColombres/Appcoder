from dataclasses import field
from msilib.schema import ListView
from sqlite3 import Cursor
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from AppCoder.forms import CursoFormulario, ProfesorFormulario
from AppCoder.models import Curso, Profesor, Estudiante
from django.views.generic import ListView ,DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy





# Create your views here.
def inicio(self):
    plantilla= loader.get_template('AppCoder/inicio.html')
    documento= plantilla.render()
    return HttpResponse(documento)


def cursos(request):
    #documento= "Pagina de cursos"
    return render(request, 'AppCoder/cursos.html')


def profesores(request):
     return render(request, 'AppCoder/profesores.html')



def estudiantes(request):
     return render(request, 'AppCoder/estudiantes.html')


def entregables(request):
     return render(request, 'AppCoder/entregables.html')

def cursoFormulario(request):
     
     if request.method== 'POST':
          miFormulario= CursoFormulario(request.POST)
          if miFormulario.is_valid():
               informacion= miFormulario.cleaned_data
               nombre= informacion ['curso']
               camada= informacion ['camada']
               curso= Curso(nombre=nombre , camada= camada )
               curso.save()
          return render (request, 'AppCoder/inicio.html')
     else:
          miFormulario= CursoFormulario()

     return render (request, 'AppCoder/cursoFormulario.html', {'miFormulario': miFormulario})

def profesorFormulario(request):
     
     if request.method== 'POST':
          miFormulario= ProfesorFormulario(request.POST)
          print(miFormulario)
          if miFormulario.is_valid:
               informacion= miFormulario.cleaned_data
               #nombre= informacion ['nombre']
               #apellido= informacion ['apellido']
               #email= informacion ['email']
               #profesion= informacion ['profesion']
               profesor= Profesor(nombre= informacion['nombre'], apellido= informacion['apellido'], email=informacion['email'] , profesion= informacion['profesion'] )
               profesor.save()
               return render (request, 'AppCoder/inicio.html')
     else:
          miFormulario= ProfesorFormulario()

     return render (request, 'AppCoder/profesorFormulario.html', {'miFormulario': miFormulario})

def busquedaCamada(request):
     return render(request, 'Appcoder/busquedaCamada.html')

def buscar(request):
     #respuesta= f"Estoy buscando la comision {request.GET['camada']}"
     if request.GET['camada']:
          camada= request.GET['camada']
          cursos= Curso.objects.filter(camada=camada)
          return render (request,'Appcoder/resultadoBusqueda.html', {'cursos':cursos, 'camada': camada})
     else:
          respuesta= "No se ha ingresado ninguna comision"
     return HttpResponse(respuesta)

def leerProfesores(request):
     profesores= Profesor.objects.all()
     contexto= {'profesores': profesores}
     return render (request, 'Appcoder/profesores.html', contexto)

#CRUD READ
def leerCurso(request):
     cursos=Curso.objects.all()
     contexto= {'cursos' : cursos}
     return render (request, 'AppCoder/cursos.html', contexto)

# CRUD DELETE

def eliminarCurso(request, camada ):
     curso= Curso.objects.get(camada= camada )
     curso.delete()
#vuelve al menu
     cursos= Curso.objects.all()
     contexto= {'cursos': cursos}
     return render(request, "AppCoder/cursos.html", contexto)

#CRUD EDITAR

def editarCurso(request, curso_camada ):

     curso= Curso.objects.get(camada= curso_camada)

     if request.method=='POST':
          miFormulario= CursoFormulario(request.POST)
          
          if miFormulario.is_valid:
               informacion= miFormulario.cleaned_data
               curso.nombre= informacion ['curso']
               curso.camada= informacion ['camada']
               curso.save()
               cursos= Curso.objects.all()
               contexto={'cursos': cursos}
               return render (request, 'AppCoder/inicio.html', contexto)
     else:
          miFormulario= CursoFormulario(initial={'curso': curso.nombre, 'camada': curso.camada})
          contexto= {'miFormulario': miFormulario, 'curso_camada': curso_camada }

          return render (request, 'AppCoder/editarCurso.html', contexto )

class Estudianteslist(ListView):
     model= Estudiante
     template_name= 'AppCoder/estudiantes.html'

class EstudianteDetalle (DetailView):
     model= Estudiante
     template_name= 'AppCoder/estudiantedetalle.html'

class EstudianteCreacion(CreateView):
     model= Estudiante
     success_url = reverse_lazy('estudiante_list')
     fields= ('nombre', 'apellido', 'email')

class EstudianteEdicion(UpdateView):
     model= Estudiante
     success_url = reverse_lazy('estudiante_list')
     fields= ('nombre', 'apellido', 'email')

class EstudianteEliminacion(DeleteView):
     model= Estudiante
     success_url = reverse_lazy('estudiante_list')


     





