from django import forms

from .models import Cliente, Empleado


class MasajeForm(forms.ModelForm):
#todos los campos de Pelicula
   class Meta:
      model = Cliente
      fields = ('nombre', 'Dia', 'Empleados')


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=('nombre','fecha_nacimiento')

def __init__ (self, *args, **kwargs):
     super(MasajeForm, self).__init__(*args, **kwargs)

     self.fields["Empleados"].widget = forms.widgets.CheckboxSelectMultiple()

     self.fields["Empleados"].help_text = "Ingrese los Empleados que participaron en los masajes"

     self.fields["Empleados"].queryset = Empleado.objects.all()
