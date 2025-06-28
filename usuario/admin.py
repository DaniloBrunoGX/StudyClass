from django.contrib import admin
from usuario.models import Perfil, Telefone, PerfilPost

# Register your models here.
admin.site.register(Perfil)
admin.site.register(Telefone)
admin.site.register(PerfilPost)
