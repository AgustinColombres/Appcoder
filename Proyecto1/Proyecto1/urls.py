"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1.view import saludo
from Proyecto1.view import saludo2
from Proyecto1.view import DiadeHoy
from Proyecto1.view import nombre_persona
from Proyecto1.view import probandotemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", saludo),
    path("saludo2/", saludo2),
    path("DiadeHoy/", DiadeHoy),
    path("nombre_persona/<nombre>/", nombre_persona),
    path("probandotemplate/", probandotemplate),
]
