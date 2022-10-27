from email.policy import default
from random import choices
from secrets import choice
from tkinter import CASCADE, image_names
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombre, apellidos, password):
        if not email:
            raise ValueError("Debe ingresar un correo")

        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            nombre=nombre,
            apellidos=apellidos,
            password=password,
        )
        return usuario

    def create_superuser(self,username,email,nombre,apellidos,password):
        usuario = self.create_user(
            email,
            username=username,
            nombre=nombre,
            apellidos=apellidos,
            password=password,
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo electronico', unique=True, max_length=254)
    nombre = models.CharField('Nombre', max_length=200, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=200, blank=True, null=True)
    informacion = models.TextField(max_length=250, null=True, blank=True)
    imagen = models.ImageField('Imagen de perfil', upload_to="perfil/",
                               height_field=None, width_field=None, max_length=200, blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_admin = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nombre', 'apellidos']

    def __str__(self):
        return f'Usuario {self.username} - {self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_admin



class Proyecto(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'Proyecto {self.title} de {self.title}'



GO = 'Go'
PHP = 'PHP'
PYTHON = 'Python'
JAVASCRIPT = 'JavaScript'
NOTHING = 'Nothing'
JAVA = 'Java'
LANGUAGES_CHOICE = (
    (NOTHING, 'Nothing'),
    (JAVASCRIPT, 'JavaScript'),
    (PYTHON, 'Python'),
    (PHP, 'PHP'),
    (JAVA, 'Java'),
    (GO, 'Go'),
)
REACT = 'React'
VUE = 'Vue'
ANGULAR = 'Angular'
LARAVEL = 'Laravel'
DJANGO = 'Django'
FLASK = 'Flask'
TECNOLOGIES_CHOICE = (
    (REACT, 'React'),
    (VUE, 'Vue'),
    (ANGULAR, 'Angular'),
    (LARAVEL, 'Laravel'),
    (DJANGO, 'Django'),
    (FLASK, 'Flask'),
)
#TOOLS_CHOICE = (
#    'VS Code',
#    'Visual Studio',
#    'Pycharm',
#    'Jupyter Notebook',
#    'Git',
#    'GitHub',
#)

class InformacionUsuario(models.Model):
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='porfolio/images')
    lenguajes = models.CharField(max_length=20, choices=LANGUAGES_CHOICE, default=NOTHING)
    tecnologias = models.CharField(max_length=20, choices=TECNOLOGIES_CHOICE, default=NOTHING)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#    herramientas = models.CharField(max_length=20, choices=TOOLS_CHOICE)

