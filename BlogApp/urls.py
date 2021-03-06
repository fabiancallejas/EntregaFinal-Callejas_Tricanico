from django.urls import path
from BlogApp.views import BlogPostLike, borrar_video,borrar_disco, editarPerfil, inicio,exito,lista_discos,agregar_video,lista_videos,detalle_videos,disco,PostDetailView,agregar_post,ver_posts,detalle_discos,autenticarse,registrarse,LogoutView,about_us,PostEdicion,PostEliminar,editar_disco
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', inicio, name='inicio'),
    path('exito/', exito, name='exito'),

    #Todo lo relacionado a discos
    path('agregar_disco/', disco, name='agregar_disco'),
    path('lista_discos/', lista_discos, name='lista_discos'),
    path('disco/<int:pk>/', detalle_discos, name='detalle_discos'),
    path('editar_disco/<int:pk>/', editar_disco, name='editar_disco'),
    path('borrar_disco/<int:pk>/', borrar_disco, name='borrar_disco'),
    path('disco-like/<int:pk>', BlogPostLike, name="disco_like"),

    #Todo lo relacionado a posts
    path('agregar_post/', agregar_post, name='agregar_post'),
    path('<slug>', PostDetailView.as_view(), name='post'),
    path('ver_posts/', ver_posts, name='ver_posts'),
    path('<slug>/edicion/', PostEdicion.as_view(), name='post_editar'),
    path('<slug>/borrar/', PostEliminar.as_view(), name='post_eliminar'),

    #Todo lo relacionado a videos
    path('agregar_video/', agregar_video, name='agregar_video'),
    path('lista_videos/', lista_videos, name= 'lista_videos'),
    path('video/<int:pk>/', detalle_videos, name='detalle_videos'),
    path('borrar_video/<int:pk>/', borrar_video, name='borrar_video'),

    #Todo lo relacionado a autenticación
    path('autenticarse/', autenticarse, name='autenticarse'),
    path('registrarse/', registrarse, name='registrarse'),
    path('salir/', LogoutView.as_view(template_name='BlogApp/salir.html'), name='salir'),
    path('editar_perfil/', editarPerfil, name='editar_perfil'),

    #About Us
    path('about_us/', about_us, name='about_us'),

]
