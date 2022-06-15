from django import forms
from django_quill.forms import QuillFormField
from embed_video.fields import EmbedVideoField
from autoslug import AutoSlugField

class Disco(forms.Form):
    nombre = forms.CharField(max_length=30)
    anio = forms.IntegerField()
    pais = forms.CharField()
    formato = forms.CharField(max_length=300)
    imagen = forms.ImageField()
    contenido = QuillFormField()

class Video(forms.Form):
	video_titulo = forms.CharField(max_length=200)
	video_cuerpo = forms.CharField()
	video_contenido = EmbedVideoField()

class Post(forms.ModelForm):
    titulo = forms.CharField()
    titulo.widget.attrs.update({'class': 'form-control'})
    imagen = forms.ImageField()
    contenido = QuillFormField()