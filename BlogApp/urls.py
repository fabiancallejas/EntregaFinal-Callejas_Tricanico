from django.urls import path
from BlogApp.views import inicio,exito,lista_discos,agregar_video,lista_videos,detalle_videos,disco,PostDetailView,agregar_post,ver_posts,detalle_discos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('exito/', exito, name='exito'),

    #Todo lo relacionado a discos
    path('agregar_disco/', disco, name='agregar_disco'),
    path('lista_discos/', lista_discos, name='lista_discos'),
    path('disco/<int:pk>/', detalle_discos, name='detalle_discos'),

    #Todo lo relacionado a posts
    path('agregar_post/', agregar_post, name='agregar_post'),
    path('<slug>', PostDetailView.as_view(), name='post'),
    path('ver_posts/', ver_posts, name='ver_posts'),

    #Todo lo relacionado a videos
    path('agregar_video/', agregar_video, name='agregar_video'),
    path('lista_videos/', lista_videos, name= 'lista_videos'),
    path('video/<int:pk>/', detalle_videos, name='detalle_videos'),

]

