from django.contrib import admin
from masajes.models import Empleado, EmpleadoAdmin, Cliente, ClienteAdmin

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Cliente, ClienteAdmin)


# Register your models here.
