from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto
from .forms import ProyectoForm


def index(request):
    return render(request, "index.html")

def lista(request):
    proyecto = Proyecto.objects.all()
    return render(request, "proyecto.html", {"Proyectos": proyecto})


def crear(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('/proyectos/')
    else:
        form = ProyectoForm()

    return render(request, "crear_proyecto.html", {"form": form})


def detalle(request, pk):
    proyecto = Proyecto.objects.get(id=pk)
    return render(request, "detalle.html", {"detalle": proyecto})

def eliminar_proyecto(request, proyecto_id):
    proyecto=Proyecto.objects.get(id=proyecto_id)
    proyecto.delete()
    return redirect('/proyectos/')