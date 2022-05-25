from multiprocessing import context
from pipes import Template
from django.http import HttpResponse
from django.template import loader
import datetime
from django.template import Template, Context


def saludo(request):
    return  HttpResponse ("Hola Django - Coder")
def saludo2(request):
    return  HttpResponse ("Hola Mundo")

def DiadeHoy(request):
    dia= datetime.datetime.now()
    texto= "Hoy es: {}".format(dia)
    return HttpResponse(texto)

def nombre_persona(self, nombre):
    resultado= "Mi nombre es <br> <br> {}".format(nombre)
    return HttpResponse(resultado)

def probandotemplate(self):
   
    nombre= "Agustin"
    apellido= "Colombres"
    listadenotas= [2,5,8,6]

    diccionario= {"nombre": nombre, "apellido": apellido, "listadenotas": listadenotas}

    #miHtml =open("template1.html")



    #plantilla=Template(miHtml.read())
    #miHtml.close()

    #miContexto= Context(diccionario)
    plantilla= loader.get_template("template1.html")
    documento= plantilla.render(diccionario)

    return HttpResponse(documento)



