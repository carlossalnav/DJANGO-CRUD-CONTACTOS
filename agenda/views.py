#from django.shortcuts import render
from django.db import models
from django.forms.formsets import formset_factory
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.forms import formset_factory
from agenda.models import Contacto
from agenda.forms import ContactoForm


class ContactoLista(ListView):
    model = Contacto
    template_name = 'base.html'

class ContactoCrear(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'agregar.html'
    success_url = reverse_lazy('inicio')

class ContactoEditar(UpdateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'editar.html'
    success_url = reverse_lazy('inicio')

class ContactoEliminar(DeleteView):
    model = Contacto
    template_name = 'verificacion.html'
    success_url = reverse_lazy('inicio')

