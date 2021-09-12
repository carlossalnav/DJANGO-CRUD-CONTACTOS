from django.db import models
from django.db.models.fields import CharField, IntegerField

ESTADOS = (
    ("AGU", "Aguascalientes"),
    ("BCN", "Baja California"),
    ("BCS", "Baja California Sur"),
    ("CAM", "Campeche"),
    ("CHP", "Chiapas"),
    ("CHH", "Chihuahua"),
    ("CMX", "Ciudad de México"),
    ("COA", "Coahuila"),
    ("COL", "Colima"),
    ("DUR", "Durango"),
    ("GUA", "Guanajuato"),
    ("GRO", "Guerrero"),
    ("HID", "Hidalgo"),
    ("JAL", "Jalisco"),
    ("MEX", "México"),
    ("MIC", "Michoacán"),
    ("MOR", "Morelos"),
    ("NAY", "Nayarit"),
    ("NLE", "Nuevo León"),
    ("OAX", "Oaxaca"),
    ("PUE", "Puebla"),
    ("QUE", "Querétaro"),
    ("ROO", "Quintana Roo"),
    ("SLP", "San Luis Potosí"),
    ("SIN", "Sinaloa"),
    ("SON", "Sonora"),
    ("TAB", "Tabasco"),
    ("TAM", "Tamaulipas"),
    ("TLA", "Tlaxcala"),
    ("VER", "Veracruz"),
    ("YUC", "Yucatán"),
    ("ZAC", "Zacatecas"),
)

TIPOS_TELEFONO = (
    (1, "Casa"),
    (2, "Teléfono móvil"),
)


class Contacto(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=120)
    fotografia = models.ImageField()
    fecha_nacio = models.DateField(default=None, null=True, blank=True)
    calle = models.CharField(max_length=255)
    numero_exterior = models.CharField(max_length=10)
    numero_interior = models.CharField(max_length=10)
    colonia = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    estado = models.CharField(max_length=3, choices=ESTADOS)
    referencias = models.TextField()
    tipo = models.IntegerField(choices=TIPOS_TELEFONO)
    alias = models.CharField(max_length=255)
    numero = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
    
    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)
    