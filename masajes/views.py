from django.shortcuts import render
from django.contrib import messages
from .forms import MasajeForm, EmpleadoForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from masajes.models import Cliente, Empleado
from django.contrib.auth.decorators import login_required

@login_required
def cliente_nueva(request):
    if request.method == "POST":
        formulario = MasajeForm(request.POST)
        if formulario.is_valid():
            cliente = Cliente.objects.create(nombre=formulario.cleaned_data['nombre'], Dia = formulario.cleaned_data['Dia'])
            for Empleado_id in request.POST.getlist('Empleados'):
                masaje = Masaje(Empleado_id=Empleado_id, Cliente_id = cliente.id)
                masaje.save()
            messages.add_message(request, messages.SUCCESS, 'Cliente Guardada Exitosamente')
            return redirect('lista_cliente')
    else:
        formulario = MasajeForm()
    return render(request, 'masajes/masaje_editar.html', {'formulario': formulario})

@login_required
def Empleada_nueva(request):
    if request.method == "POST":
        formu = EmpleadoForm(request.POST)
        if formu.is_valid():
            empleado = Empleado.objects.create(nombre=formu.cleaned_data['nombre'], fecha_nacimiento = formu.cleaned_data['fecha_nacimiento'])
            messages.add_message(request, messages.SUCCESS, 'Empleado Guardada Exitosamente')
            return redirect('Empleado_listar')
    else:
        formu = EmpleadoForm()
    return render(request, 'masajes/crear_empleado.html', {'formu': formu})

@login_required
def cliente_edit(request, pk):
    pub = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = MasajeForm(request.POST, instance=pub)
        if form.is_valid():
            pub = form.save(commit=False)
            pub.save()
        return redirect('lista_cliente')
    else:
        form = MasajeForm(instance=pub)
    return render(request, 'masajes/cliente_edit.html', {'form': form})

@login_required
def Empleado_edit(request, pk):
    ada = get_object_or_404(Empleado, pk=pk)
    if request.method == "POST":
        formf = EmpleadoForm(request.POST, instance=ada)
        if formf.is_valid():
            ada = formf.save(commit=False)
            ada.save()
        return redirect('Empleado_listar')
    else:
        formf = EmpleadoForm(instance=ada)
    return render(request, 'masajes/edit_empleado.html', {'formf': formf})


def lista_cliente(request):
    pub = Cliente.objects.all()
    return render(request, 'masajes/list_masaje.html', {'pub' : pub})

def Empleado_listar(request):
    ada = Empleado.objects.all()
    return render(request, 'masajes/Empleado_list.html', {'ada' : ada})

@login_required
def cliente_remove(request, pk):
    pub = get_object_or_404(Cliente, pk=pk)
    pub.delete()
    return redirect('lista_cliente')

@login_required
def Empleado_remove(request, pk):
    pub = get_object_or_404(Empleado, pk=pk)
    pub.delete()
    return redirect('Empleado_listar')


# Create your views here.
