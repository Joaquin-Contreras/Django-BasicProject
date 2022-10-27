from django import forms
from portafolio.models import Usuario
from .models import Proyecto, InformacionUsuario


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['title','descripcion','url']

class UsuarioInformacion(forms.ModelForm):
    class Meta:
        model = InformacionUsuario
        fields = ['descripcion','lenguajes','tecnologias']

class FormularioUsuario(forms.ModelForm):
    
    password1 = forms.CharField(label = 'contraseña', widget=forms.PasswordInput(
        attrs= {
            'class': 'form-control',
            'placeholder': 'Contraseña...',
            'id': 'password1',
            'required': 'required',
        }
    ))
    password2 = forms.CharField(label = 'contraseña repetida', widget=forms.PasswordInput(
        attrs= {
            'class': 'form-control',
            'placeholder': 'Repetir contraseña...',
            'id': 'password',
            'required': 'required',
        }
    ))
    
    class Meta:
        model = Usuario
        fields = ['username','email','nombre','apellidos','password']
        widgets = {
            'email': forms.EmailInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Correo Electronico',
                }
            ),
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                }
            ),
            'apellidos': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Apellido/s',
                }
            ),
            'username': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Nombre de usuario',
                }
            ),
        }



class FormularioInicioSesion(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id':'loginEmail',
                'type':'email',
                'class':'form-control',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id':'loginPassword',
                'type':'password',
                'class':'form-control',
            }
        )
    )