from django import forms
from django_quill.forms import QuillFormField
from embed_video.fields import EmbedVideoField
from autoslug import AutoSlugField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DiscoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    anio = forms.IntegerField()
    pais = forms.CharField()
    formato = forms.CharField(max_length=300)
    imagen = forms.ImageField()
    contenido = QuillFormField()

class VideoFormulario(forms.Form):
	titulo = forms.CharField(max_length=200)
	cuerpo = forms.CharField()
	video = EmbedVideoField()

class Post(forms.ModelForm):
    titulo = forms.CharField()
    titulo.widget.attrs.update({'class': 'form-control'})
    imagen = forms.ImageField()
    contenido = QuillFormField()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Modificar Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Modificar Nombre")
    last_name = forms.CharField(label="Modificar Apellido")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name','last_name']
        help_texts={k:"" for k in fields}
    
