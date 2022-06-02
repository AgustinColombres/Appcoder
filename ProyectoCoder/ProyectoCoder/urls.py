
from django.contrib import admin
from django.urls import path, include
#from AppCoder.views import cursos, profesores, entregables, estudiantes, inicio
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

