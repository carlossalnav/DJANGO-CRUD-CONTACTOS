from agenda.models import Contacto
from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactoForm

def inicio(request):
    template = get_template("base.html")
    contactos = Contacto.objects.all()
    context = {"titulo": "Inicio", "contactos": contactos}
    return HttpResponse(template.render(context), request)

def agregar(request):
    if request.method == "POST":
        contacto_form = ContactoForm(request.POST, request.FILES)
        if contacto_form.is_valid():
            contacto_form.save()
            return redirect('inicio')

    else:
        contacto_form = ContactoForm()

    context = {'contacto_form': contacto_form}
    return render(request, "agregar.html", context)

def editar(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    if request.method == "POST":

        contacto_form = ContactoForm(request.POST, request.FILES, instance=contacto)

        if contacto_form.is_valid():
            contacto_form.save()
            
            return redirect('inicio')
            

    else:
        contacto_form = ContactoForm(instance=contacto)

    context = {'contacto_form': contacto_form}
    return render(request, "editar.html", context)


def eliminar(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    contacto.delete()
    return redirect('inicio')