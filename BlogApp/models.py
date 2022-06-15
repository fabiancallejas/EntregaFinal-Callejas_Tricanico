from django.db import models
from django_quill.fields import QuillField
from embed_video.fields  import  EmbedVideoField
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model


#FormatoCD

# Create your models here.

class Disco (models.Model):
    nombre = models.CharField(max_length=30)
    anio = models.IntegerField()
    pais = models.CharField(max_length=30)
    formato = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='portadadiscos', null=True, blank = True)
    contenido = QuillField()

class Videos(models.Model):
	titulo = models.CharField(max_length=200)
	cuerpo = models.TextField()
	video = EmbedVideoField()

	class  Meta:
		verbose_name_plural = "Video"

	def  __str__(self):
		return  str(self.titulo) if  self.titulo  else  " "

#Blog

User = get_user_model()

class Autor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="")
    def __str__(self):
        return self.usuario.username

class Categorias(models.Model):
    titulo = models.CharField(max_length=20)
    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='titulo')
    resumen = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="imagenesPost", null=True, blank=True)
    contenido = QuillField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    def __str__(self):
        return self.slug
