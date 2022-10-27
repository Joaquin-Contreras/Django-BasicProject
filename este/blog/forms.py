from django import forms
from portafolio.models import Usuario
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','contenido', 'topico']