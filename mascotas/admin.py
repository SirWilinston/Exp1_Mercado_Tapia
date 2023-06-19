from django.contrib import admin

from mascotas.models import Asociado, Comuna, TipoSocio, Producto

# Register your models here.
admin.site.register(Asociado)
admin.site.register(Comuna)
admin.site.register(TipoSocio)
admin.site.register(Producto)