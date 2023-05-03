from django.urls import path

from generator.views import procesar_formulario


urlpatterns = [
    path('/', procesar_formulario, name='procesar_formulario'),
]

