from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from datetime import datetime
from .forms import CitaForm
from .models import Cita

# Vista principal de Citas
def CitasIndex(request):
    #consultar Citas
    Citas = Cita.objects.all()
   

    #Consultar Citas
    Cita_list = Cita.objects.all()
    #Configurar paginación cada 20 citas
    paginator = Paginator(Cita_list, 20)

    #Obtener página
    page_number = request.GET.get('page',0)
    page_obj = paginator.get_page(page_number)
    #Obtener el template
    template = loader.get_template("Citas.html")
    #Agregar el contexto
    context = {"page_obj": page_obj,"citas":Citas}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

#Vista para ver detalles de un autor
def detalleCitas(request, id):
    #Consultar Citas
    Citas = Cita.objects.get(id=id)           
    #Consultar datos de Citas
    context = {'cita':Citas}
    #Obtener el template
    template = loader.get_template("detalleCitas.html")

    return HttpResponse(template.render(context,request))

# Vista principal de Gestión de Citas
def gestionCitas(request):
    
    # Consultar Citas
    
    cita_list = Cita.objects.all().order_by('id')
    
    # Configurar paginación cada 20 Citas
    paginator = Paginator(cita_list, 20)

    # Obtener página
    page_number = request.GET.get('page', 0)
    page_obj = paginator.get_page(page_number)

    # Obtener el template
    template = loader.get_template("gestionCitas.html")

    # Agregar el contexto
    context = {"page_obj": page_obj}

    # Retornar respuesta http
    return HttpResponse(template.render(context, request))

# Vista para crear Citas
def crearCitas(request):
    #Obtener el template
    template = loader.get_template("crearCitas.html")
    #Generar Formulario
    if request.method == "POST":
        form = CitaForm(request.POST or None, request.FILES)
        if form.is_valid():
            #obtener datos del formulario
            Cita_nueva = form.save(commit=False)
            #Asignar fecha de creación
            Cita_nueva.fecha_creacion = datetime.now()
            #Guardar Cita
            Cita_nueva.save()
            return redirect('gestionCitas')
    else:
        form = CitaForm()
    #Crear contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

# Vista de Citas
def editarCitas(request,id):
    #Obtener el template
    template = loader.get_template("editarCitas.html")
    #Buscar Cita
    obj = get_object_or_404(Cita, id = id)
    #formulario que contiene la instancia
    form = CitaForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('gestionCitas')   
    #Agregar el contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

# Vista de Cita
def eliminarCitas(request,id):
    #Obtener el template
    template = loader.get_template("eliminarCitas.html")
    #Buscar la Cita
    obj = get_object_or_404(Cita, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('gestionCitas')
    #Agregar el contexto
    context = {}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))
   

def verCitas(request, cita_id):  # Debe coincidir con el nombre en la URL
    cita = get_object_or_404(Cita, id=cita_id)
    return render(request, 'verCitas.html', {'cita': cita})

