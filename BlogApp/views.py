from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .forms import Disco,Video
from .models import Disco,Videos,Post
from django import forms

# Create your views here.
def inicio (request):
    documento = f"Página de Inicio"
    return render(request, 'BlogApp/index.html')

class NewForm(forms.ModelForm):
   class Meta:
      model=Disco
      fields="__all__"
## Todo lo relacionado a Discografía

def disco(request):
    if request.method =="POST":
        form = NewForm (request.POST)
        if form.is_valid():
            datosdisco = form.cleaned_data
        nombre = datosdisco ['nombre']
        anio = datosdisco ['anio']
        pais = datosdisco ['pais']
        formato = datosdisco ['formato']
        imagen = datosdisco ['imagen']
        contenido = datosdisco ['contenido']
        disco = Disco(nombre=nombre, anio=anio, pais=pais, formato=formato, imagen=imagen, contenido=contenido)
        disco.save()
        return render(request, 'BlogApp/exito.html')
    else:
        form = NewForm()
    return render(request, 'BlogApp/agregar_disco.html', {'form': form})

def lista_discos(request):
    ver_discos = Disco.objects.all()
    return render(request, "BlogApp/lista_discos.html", {"ver_discos": ver_discos})

def detalle_discos(request,pk):
	Disc = Disco.objects.get(pk=pk)
	contexto = {
	'Disc': Disc,
	}
	return  render(request, 'BlogApp/detalle_discos.html', contexto)

## Todo lo relacionado a Videos
class NewForm2(forms.ModelForm):
   class Meta:
      model=Videos
      fields="__all__"

def agregar_video(request):
    if request.method =="POST":
        form = NewForm2 (request.POST)
        if form.is_valid():
            datosvideo = form.cleaned_data
        titulo = datosvideo ['titulo']
        cuerpo = datosvideo ['cuerpo']
        video = datosvideo ['video']
        video_completo = Videos(titulo=titulo, cuerpo=cuerpo, video=video)
        video_completo.save()
    
        Tut = Videos.objects.all()
        context = { 
            'Tut': Tut, 
        }
        return  render(request, 'BlogApp/lista_videos.html', context)
    else:
        form = NewForm2()
    return render(request, 'BlogApp/agregar_video.html', {'form': form})

def lista_videos(request):
	Tut = Videos.objects.all()
	context = {
	'Tut': Tut,
	}
	return  render(request, 'BlogApp/lista_videos.html', context)

def detalle_videos(request,pk):
	Tut = Videos.objects.get(pk=pk)
	context = {
	'Tut': Tut,
	}
	return  render(request, 'BlogApp/detalle_videos.html', context)

def exito (self):
    documento = f"Llegamos a guardar!"
    return HttpResponse(documento)

def blog(request):
    context = {}
    return render(request, "BlogApp/blog.html", context)

## Post - Usando DetailView
class PostDetailView(DetailView):
    model = Post
    template_name = "BlogApp/detalle_posts.html"
    slug_field = "slug"

## Post - Crear un Post
class NewForm3(forms.ModelForm):
   class Meta:
      model=Post
      fields="__all__"
      slug_field = "slug"

def agregar_post(request):
    if request.method =="POST":
        form = NewForm3 (request.POST, request.FILES)
        if form.is_valid():
            datospost = form.cleaned_data
        titulo = datospost ['titulo']
        resumen = datospost ['resumen']
        imagen = datospost ['imagen']
        contenido = datospost ['contenido']
        autor = datospost ['autor']
        postcompleto = Post(titulo=titulo, resumen=resumen, imagen=imagen, contenido=contenido, autor=autor)
        postcompleto.save()

        return render(request, 'BlogApp/exito.html')
    else:
        form = NewForm3()
    return render(request, 'BlogApp/agregar_post.html', {'form': form})


def ver_posts(request):
    posts = Post.objects.all()
    contexto = {'posts':posts}    
    return render (request, 'BlogApp/lista_post.html', contexto)
