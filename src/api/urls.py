from django.urls import path
from .import views

app_name = 'api'

urlpatterns = [
    path('coordinadores/', views.CoordinadorListAPIView.as_view(), name='listar_coordinadores'),
    path('coordinadores/<int:pk>/', views.CoordinadorRetrieveAPIVIEW.as_view(), name='buscar_coordinador'),
    path('empleados/', views.EmpleadoListAPIView.as_view(), name='listar_empleados'),
    path('empleados/<int:pk>', views.EmpleadoRetrieveAPIView.as_view(), name='buscar_empleado'),
    path('reservas/', views.ReservaListAPIView.as_view(), name='listar_reservas'),
    path('reservas/<int:id>', views.ReservaRetrieveAPIView.as_view(), name='buscar_reserva'),
]
