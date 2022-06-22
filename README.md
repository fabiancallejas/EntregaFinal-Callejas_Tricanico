# Melanie C Records - Blog

Videos Presentación del Blog: https://drive.google.com/drive/folders/1LFh-onoFdGPVDZefqHe3CBW8UwljMYIe?usp=sharing


URL del blog en Python Anywhere: https://melaniecrecords.pythonanywhere.com/

Usuario registrado en la web: Fabiantoti / contrasenia1

Usuario Admin: administrador / admin

## Dependencias:

pip install django-quill-editor

pip install django-embed-video

pip install django-widget-tweaks

pip install django-autoslug

pip install pillow

**La siguiente dependencia no se usa, pero no pudimos desinstalarla**

pip install django-countries 



## Explicación del blog y sus funcionalidades:

Este blog seria para registrar discos, videos (con link a YouTube) y un blog con entradas.

Sus funcionalidades que tiene son las de registro, autenticación, edición de usuario y salida.

## Notas a tener en cuenta:

El blog es una mezcla, ya sea tanto como de Python como con funciones de Django. Comentamos esto porque en algunas secciones se utilizan vistas/forms de Django mientras que en otras se utiliza Python. La idea era tratar de abarcar todo lo visto en las clases.

## Explicación de secciones:



**Discografia**

_Sección para agregar discos, portadas e informacion._

· Agregar Discos

· Ver Lista de Discos


**Implementación destacada:** Posibilidad de dar like, unlike y contador de likes a Discos.



**Videografia**

_Seccion para agregar videos (links de YouTube) y poder verlos en forma de lista, con su preview correspondiente._

· Agregar Videos

· Ver Lista de Videos

**Implementación destacada:** App para ver videos en el browser.


**Blog**

_Seccion de Blogs, donde se pueden ver o agregar blogs._

· Crear Nueva Entrada

· Resumen

**Implementación destacada:** Rich Text Field (Quill Field), Página de confirmación de eliminación



**Menú de autenticación**

_Usuario invitado:_

· Autenticarse

· Registrarse

_Usuario registrado:_

· Editar Perfil

· Salir

## Tickets de trabajo

· Primeros models, Templates: Fabián Callejas / Marianella Tricánico

· Autenticación, Registro, Edición de Perfil, Modelos: Marianella Tricánico

· Diferentes Bugs: Marianella Tricánico

· Login en secciónes, 404 Error, Otras Páginas: Fabián Callejas

· Editar / Eliminar Posts, Templates: Fabián Callejas

· Bugs / About Us: Fabián Callejas 

· Editar / Borrar Discos, Diferentes Bugs: Marianella Tricánico

· Like y Bugs: Fabián Callejas

· Deploy a PythonAnywhere: Marianella Tricánico / Fabián Callejas





## Mejoras que por falta de tiempo no fueron incluidas:

· Manejo de errores en los formularios / imagenes incorrectas.

· Dos imagenes fueron harcodeadas en vez de guardar el recurso en el lugar.

· Borrar dependencias que no fueron utilizadas

