from sqlite3 import Cursor
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from AppCoder.forms import CursoFormulario
from AppCoder.models import Curso




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
