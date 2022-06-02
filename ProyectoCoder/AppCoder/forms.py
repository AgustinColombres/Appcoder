from django import forms

class CursoFormulario(forms.Form):
    curso= forms.CharField(max_length=50)
    camada= forms.IntegerField()