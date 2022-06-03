from django.db import models

class Curso(models.Model):
    nombre= models.CharField(max_length=40)
    camada= models.IntegerField()

class estudiantes(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Profesor (models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

class entregables(models.Model):
    nombre= models.CharField(max_length=30)
    fechadeEntrega= models.DateField()
    entregado= models.BooleanField()




