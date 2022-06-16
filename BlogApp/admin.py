from django.contrib import admin
from .models import *
from embed_video.admin  import  AdminVideoMixin


class  videoAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass
admin.site.register(Disco)
admin.site.register(Videos, videoAdmin)
admin.site.register(Post)

