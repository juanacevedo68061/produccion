from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def listar(request):
    #usuarios = User.objects.all() #solo para desarrollo
    usuarios = User.objects.filter(is_staff=True)
    return render(request,'list_usuarios.html', {"usuarios": usuarios})

def eliminar(request, usuario_id):
    usuario=User.objects.get(id=usuario_id)
    usuario.delete()
    return redirect('/usuarios/')

def agregar(request, usuario_id):
    usuario=User.objects.get(id=usuario_id)
    usuario.is_staff=False
    usuario.save()
    return redirect('/usuarios/')