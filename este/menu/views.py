from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from portafolio.forms import FormularioUsuario
from portafolio.models import Usuario

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


def crearCuenta(request):
    if request.method == 'GET':
        return render(request, 'crearCuenta.html', {
            'form': FormularioUsuario
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                """
                form = FormularioUsuario(request.POST)
                if form.is_valid():
                    form.save()
                """


                
                user = get_user_model().objects.create(
                    username = request.POST['username'],
                    email = request.POST['email'],
                    nombre = request.POST['nombre'],
                    apellidos = request.POST['apellidos'],
                    password= request.POST['password1']
                )
                user.set_password(request.POST['password1'])
                user.save()
                
                return redirect("iniciarSesion")
            except ValueError:
                print(ValueError)
                return render(request, 'crearCuenta.html', {
                    'form': FormularioUsuario,
                    'error': "Ya existe ese usuario",
                })
        else:
            return render(request, 'crearCuenta.html', {
                'form': FormularioUsuario,
                'error': "Las contraseñas deben ser iguales"
            })


def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'iniciarSesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciarSesion.html', {
                'form': AuthenticationForm,
                'error': "User or password is incorrect"
            })
        else:
            login(request, user)
            return redirect('/')

@login_required
def cerrarSesion(request):
    logout(request)

    return redirect("inicio")

def buscar(request):
    busqueda=request.GET.get('busqueda','')
    usuario = Usuario.objects.filter(username__icontains=busqueda)
    print(usuario)
    return render(request,"borrar.html", {
        'usuario':usuario,
        'funciona': "FUNCIONAAA",
    })


