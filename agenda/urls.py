from django.urls import path
from . import views


urlpatterns = [
    path("", views.ContactoLista.as_view(), name="inicio"),
    path("agregar/", views.ContactoCrear.as_view(), name="agregar" ),
    path("editar/<int:pk>", views.ContactoEditar.as_view(), name="editar"),
    path("eliminar/<int:pk>", views.ContactoEliminar.as_view(), name="eliminar"),
]
