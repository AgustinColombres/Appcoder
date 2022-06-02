from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


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
    return render (request, 'AppCoder/cursoFormulario.html')
