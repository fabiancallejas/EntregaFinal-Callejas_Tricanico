# EntregaFinal-Callejas_Tricanico

Melanie C Records - Blog

URL: https://melaniecrecords.pythonanywhere.com/

Dependencias:
pip install django-quill-editor
pip install django-embed-video
pip install django-widget-tweaks
pip install django-autoslug
pip install pillow
# la siguiente dependencia no se usa, pero no pudimos desinstalarla
pip install django-countries 

- Explicación del blog y sus funcionalidades:

Este blog seria para registrar discos, videos (con link a YouTube) y un blog con entradas.
Sus funcionalidades que tiene son las de registro, autenticación, edición de usuario y salida.

- Explicacisón de secciones:

-- Discografia
Sección para agregar discos, portadas e informacion.
· Agregar Discos
· Ver Lista de Discos

Implementación destacada: Posibilidad de dar like, unlike y contador de likes a videos.

-- Videografia
Seccion para agregar videos (links de YouTube) y poder verlos en forma de lista, con su preview correspondiente.
· Agregar Videos
· Ver Lista de Videos

Implementación destacada: App para ver videos en el browser.

-- Blog
Seccion de Blogs, donde se pueden ver o agregar blogs.

· Crear Nueva Entrada
· Resumen

Implementación destacada: Rich Text Field (Quill Field)

-- Menú de autenticación:
Usuario invitado:
· Autenticarse
· Registrarse

Usuario registrado:
· Editar Perfil
· Salir


- Tickets de trabajo

· Primeros models, Templates: Fabián Callejas / Marianella Tricánico
· Autenticación, Registro, Edición de Perfil, Modelos: Marianella Tricánico
· Diferentes Bugs: Marianella Tricánico
· Login en secciónes, 404 Error, Otras Páginas: Fabián Callejas
· Editar / Eliminar Posts, Templates: Fabián Callejas
· Bugs / About Us: Fabián Callejas 
· Editar / Borrar Discos, Diferentes Bugs: Marianella Tricánico
· Like y Bugs: Fabián Callejas
· Deploy a PythonAnywhere: Marianella Tricánico / Fabián Callejas

- Mejoras que por falta de tiempo no fueron incluidas:
· Manejo de errores en los formularios / imagenes incorrectas.
· Dos imagenes fueron harcodeadas en vez de guardar el recurso en el lugar.
· Borrar dependencias que no fueron utilizadas