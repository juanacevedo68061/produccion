from django.urls import include, path
from django.contrib.auth.views import LogoutView
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('proyectos/', views.lista, name="proyectos"),
    path('nuevo/', views.crear, name="nuevo"),
    path('proyectos/<int:pk>', views.detalle, name="detalle"),
    path('<int:proyecto_id>/', views.eliminar_proyecto, name="eliminar"),
    path('usuarios/', include('Usuarios.urls')),
    path('accounts/', include('allauth.urls')),
    path('salir/', LogoutView.as_view()),
]