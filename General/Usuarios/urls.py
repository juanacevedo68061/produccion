from django.urls import path
from .views import listar, eliminar, agregar

urlpatterns = [
    path('', listar),
    path('eliminar/<int:usuario_id>', eliminar, name='eliminacion'),
    path('<int:usuario_id>/', agregar, name='agregar'),
]