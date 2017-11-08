from django.db import models
from django.contrib import admin


#Define la clase Actor, esta tabla no se relaciona con nadie más.

class Empleado(models.Model):
   nombre  =   models.CharField(max_length=30)
   fecha_nacimiento = models.DateField()
   def __str__(self):
     return self.nombre

class Cliente(models.Model):
   nombre    = models.CharField(max_length=60)
   Dia      = models.IntegerField()
   Empleados   = models.ManyToManyField(Empleado, through='Masaje')
   def __str__(self):
     return self.nombre

class Masaje (models.Model):
   Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
   Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class MasajeInLine(admin.TabularInline):
   model = Masaje
   extra = 1

class EmpleadoAdmin(admin.ModelAdmin):
   inlines = (MasajeInLine,)

class ClienteAdmin (admin.ModelAdmin):
   inlines = (MasajeInLine,)
# Create your models here.
