from django import forms
from django.db.models import fields
from agenda.models import Contacto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ('nombre','apellidos','fotografia','fecha_nacio','calle','numero_exterior','numero_interior','colonia','municipio','estado','referencias','tipo','alias','numero')