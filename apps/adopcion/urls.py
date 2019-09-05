from django.urls import path
from apps.adopcion.views import index
#from apps.mascota.views import index


urlpatterns = [
    path('index', index),
]