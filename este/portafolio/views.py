import logging
from django.shortcuts import render, redirect, get_object_or_404
from .models import InformacionUsuario, Proyecto
from django.contrib.auth.decorators import login_required
from .forms import ProyectoForm
from portafolio.models import Usuario, InformacionUsuario
from portafolio.forms import FormularioUsuario, UsuarioInformacion

# Create your views here.


def Perfil(request):
    proyectos = Proyecto.objects.filter(user=request.user)
    user = request.user
    infoUser = InformacionUsuario.objects.filter(user=request.user)
    print(infoUser.values)
    return render(request, 'perfil.html', {
        'proyectos': proyectos,
        'user': user,
        'infoUser': infoUser,
    })


@login_required
def crearProyecto(request):
    if request.method == 'GET':
        return render(request, 'agregarProyecto.html', {
            'form': ProyectoForm
        })
    else:
        try:
            form = ProyectoForm(request.POST)
            print(form)
            nuevoProyecto = form.save(commit=False)
            nuevoProyecto.user = request.user
            nuevoProyecto.save()
            return redirect('/portfolio')
        except ValueError:
            return render(request, 'agregarProyecto.html', {
                'form': ProyectoForm,
                'error': "ASDADSSDASDADS",
            })


@login_required
def eliminarProyecto(request, proyecto_id):

    proyecto = get_object_or_404(Proyecto, pk=proyecto_id, user=request.user)

    if request.method == 'POST':
        proyecto.delete()
        return redirect('/portfolio')


@login_required
def proyecto_detalle(request, proyecto_id):

    if request.method == 'GET':
        proyecto = get_object_or_404(Proyecto, pk=proyecto_id)

        form = ProyectoForm(instance=proyecto)
        return render(request, 'proyecto_detalle.html', {
            'proyecto': proyecto,
            'form': form,
        })

    try:
        proyecto = get_object_or_404(
            Proyecto, pk=proyecto_id, user=request.user)
        form = ProyectoForm(request.POST, instance=proyecto)
        form.save()
        return redirect('/portfolio')
    except ValueError:
        return render(request, 'proyecto_detalle.html', {
            'proyecto': proyecto,
            'form': form,
            'error': 'Error',
        })


@login_required
def modificarProyecto(request, proyecto_id):
    if request.method == 'GET':
        proyecto = get_object_or_404(
            Proyecto, pk=proyecto_id, user=request.user)

        form = ProyectoForm(instance=proyecto)
        return render(request, 'modificarProyecto.html', {
            'proyecto': proyecto,
            'form': form,
        })
    try:
        proyecto = get_object_or_404(
            Proyecto, pk=proyecto_id, user=request.user)

        form = ProyectoForm(request.POST, instance=proyecto)
        form.save()
        return redirect("/portfolio")
    except ValueError:

        return render(request, 'modificarProyecto.html', {
            'proyecto': proyecto,
            'form': form,
            'error': 'Ha ocurrido un error'
        })


@login_required
def modificarPerfil(request, user_id):
    if request.method == 'GET':

        form = UsuarioInformacion(instance=InformacionUsuario)
        return render(request, 'modificarPerfil.html', {
            'form': form,
        })

    try:
        form = UsuarioInformacion(instance=InformacionUsuario)
        form.save()
        return redirect("/portfolio")
    except ValueError:
        return render(request, 'modificarPerfil.html', {
            'form': form,
            'error': 'Ha ocurrido un error'
        })
