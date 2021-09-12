from django import forms
from django.db.models import fields
from agenda.models import Contacto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = [
            'nombre',
            'apellidos',
            'fotografia',
            'fecha_nacio',
            'calle',
            'numero_exterior',
            'numero_interior',
            'colonia',
            'municipio',
            'estado',
            'referencias',
            'tipo',
            'alias',
            'numero'
        ]
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'fotografia': 'Fotografía',
            'fecha_nacio': 'Fecha de Nacimiento (dd/mm/aaaa)',
            'calle': 'Calle',
            'numero_exterior': 'Número Exterior',
            'numero_interior': 'Número Interior',
            'colonia': 'Colonia',
            'municipio': 'Municipio',
            'estado': 'Estado',
            'referencias': 'Referencias',
            'tipo': 'Tipo',
            'alias': 'Alias',
            'numero': 'Número de Teléfono'
        }