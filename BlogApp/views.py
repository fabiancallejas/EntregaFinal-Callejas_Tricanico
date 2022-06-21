from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .forms import DiscoFormulario,UserRegistrationForm,UserEditForm
from .models import Disco,Videos,Post
from django import forms
from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def inicio (request):
    return render(request, 'BlogApp/index.html')

## Todo lo relacionado a Discografía


@login_required
def disco(request):
    if request.method =="POST":
        form = DiscoFormulario (request.POST, request.FILES)
        if form.is_valid():
            datosdisco = form.cleaned_data
        nombre = datosdisco ['nombre']
        anio = datosdisco ['anio']
        pais = datosdisco ['pais']
        formato = datosdisco ['formato']
        imagen = datosdisco ['imagen']
        contenido = datosdisco ['contenido']
        disco_completo = Disco(nombre=nombre, anio=anio, pais=pais, formato=formato, imagen=imagen, contenido=contenido)
        disco_completo.save()
        return render(request, 'BlogApp/exito.html')
    else:
        form = DiscoFormulario()
    return render(request, 'BlogApp/agregar_disco.html', {'form': form})

def lista_discos(request):
    ver_discos = Disco.objects.all()
    return render(request, "BlogApp/lista_discos.html", {"ver_discos": ver_discos})

def detalle_discos(request,pk):
    Disc = Disco.objects.get(id=pk)
    likes_connected = get_object_or_404(Disco, id=pk)
    liked = False
    if likes_connected.likes.filter(id=request.user.id).exists():
        liked = True
        
    number_of_likes = likes_connected.number_of_likes()
    contexto = {
    'pk': pk,
	'Disc': Disc,
    'post_is_liked': liked,
    'number_of_likes':number_of_likes
    }
    return  render(request, 'BlogApp/detalle_discos.html', contexto)

def BlogPostLike(request, pk):
    post = get_object_or_404(Disco, id=request.POST.get('blogpost_id'))
    print("like")
    print(pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('detalle_discos', args=[str(pk)]))



@login_required
def editar_disco(request, pk):
    disco = Disco.objects.get(id=pk)

    if request.method == 'POST':
        miDisco = DiscoFormulario(request.POST,request.FILES)

        if miDisco.is_valid():
            inf = miDisco.cleaned_data
        nombre = inf ['nombre']
        anio = inf ['anio']
        formato = inf ['formato']
        imagen = inf ['imagen']
        contenido = inf ['contenido']
        datos = Disco(nombre=nombre, anio=anio, formato=formato, imagen=imagen, contenido=contenido)
        datos.save()
        return render (request, 'BlogApp/index.html')
    else:
        miDisco = DiscoFormulario(initial= {'nombre':disco.nombre,'anio':disco.anio,'formato':disco.formato,'contenido':disco.contenido,'imagen':disco.imagen })
        contexto = {'DiscoFormulario':miDisco,'pk':pk}
        return render(request, 'BlogApp/editar_disco.html', contexto)

@login_required
def borrar_disco (request,pk):
    disco = Disco.objects.get(id=pk)
    disco.delete()
    discos = Disco.objects.all()
    contexto = {'ver_discos':discos}
    return render (request, "BlogApp/lista_discos.html", contexto)


## Todo lo relacionado a Videos
class NewForm2(forms.ModelForm):
   class Meta:
      model=Videos
      fields="__all__"

@login_required
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
    'pk': pk
	}
	return  render(request, 'BlogApp/detalle_videos.html', context)

@login_required
def borrar_video (request,pk):
    video = Videos.objects.get(id=pk)
    video.delete()
    videos = Videos.objects.all()
    contexto = {'ver_videos':videos}
    return render (request, "BlogApp/lista_videos.html", contexto)

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

@login_required
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


#UpdateView
class PostEdicion(LoginRequiredMixin,UpdateView):
    model = Post
    success_url = reverse_lazy('ver_posts')
    fields = ['titulo', 'resumen', 'imagen','autor','contenido']

#DeleteView
class PostEliminar(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('ver_posts')

def ver_posts(request):
    posts = Post.objects.all()
    contexto = {'posts':posts}
    return render (request, 'BlogApp/lista_post.html', contexto)

## Relacionado a Autenticación

##Autenticación
def autenticarse(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      usuario = form.cleaned_data.get('username')
      contrasenia = form.cleaned_data.get('password')
      # Autenticación de usuario
      user = authenticate(username=usuario, password=contrasenia) # Si este usuario existe me lo trae
      if user is not None:
        login(request,user) # Si existe, lo loguea
        return render(request, 'BlogApp/index.html', {'mensaje': f'Bienvenido {usuario}'})
      else:
        return render(request, 'BlogApp/index.html', {'mensaje': 'Error, datos incorrectos'})
    else:
      return render(request,'BlogApp/index.html', {'mensaje': 'Error, formulario erróneo'})
  form = AuthenticationForm() # Creo un formulario vacío si vengo por GET
  return render(request, 'BlogApp/login.html', {'form':form})

#Registrarse
def registrarse(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      usuario = form.cleaned_data['username']
      form.save()
      return render(request, 'BlogApp/index.html', {'mensaje': f'Usuario {usuario} creado'})
    else:
      return render(request, 'BlogApp/index.html', {'mensaje': 'Error, no se pudo crear el usuario'})
  else:
    form = UserRegistrationForm()
    return render(request, 'BlogApp/registrarse.html', {'form':form})

#Editar Perfil
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()

            return render(request, 'BlogApp/index.html')
    else:
        form = UserEditForm(initial={'email':usuario.email, 'first_name':usuario.first_name, 'last_name':usuario.last_name})
    return render(request, 'BlogApp/editar_perfil.html',{"form":form, "usuario":usuario} )

#About Us 
def about_us (request):
    return render(request, 'BlogApp/about_us.html')


