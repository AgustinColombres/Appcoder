from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    curso= forms.CharField(max_length=50)
    camada= forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class UserRegisterForm (UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput)

class Meta:
    model= User
    fields= ['username', 'email', 'password1', 'password2']
    #saca los mensajes de ayuda
    help_texts= {k:"" for k in fields}

class UserEditForm (UserCreationForm):
    last_name= forms.CharField(label='Modificar el Apellido')
    first_name= forms.CharField(label='Modificar el Nombre')
    email= forms.EmailField(required=True)
    password1= forms.CharField(label='Modificar Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput)
    
class Meta:
    model= User
    fields= ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    #saca los mensajes de ayuda
    help_texts= {k:"" for k in fields}