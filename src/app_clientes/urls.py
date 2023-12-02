from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('listado/', views.listado_clientes, name='listado_clientes'),
]
