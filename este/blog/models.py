from django.db import models
from portafolio.models import Usuario
import datetime

# Create your models here.

class Topico(models.Model):
    tema = models.CharField(max_length=200)

    def __str__(self):
        return self.tema

class Post(models.Model):
    titulo = models.CharField(max_length=100) 
    contenido = models.TextField()
    imagen = models.ImageField(upload_to= 'blog/images', null=True)
    fecha = models.DateField(datetime.date.today) 
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    topico = models.ForeignKey(Topico, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.titulo} + {self.user}'