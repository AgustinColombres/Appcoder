from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.
def curso(self):
    curso=Curso(nombre= "Desarrollo Web", camada=15239)
    curso.save()
    documento= f"Curso:{curso.nombre} - camaada:{curso.camada}"
    return HttpResponse(documento)