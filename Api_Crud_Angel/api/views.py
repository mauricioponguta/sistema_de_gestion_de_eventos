from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import (
    Sede,
    Organizador,
    Evento,
    Asistente,
    Inscripcion,
    Pago,
    Conferencia,
    Patrocinador,
)

from .serializers import (
    SedeSerializer,
    OrganizadorSerializer,
    EventoSerializer,
    AsistenteSerializer,
    InscripcionSerializer,
    PagoSerializer,
    ConferenciaSerializer,
    PatrocinadorSerializer,
)


# Crud de tabla Sede (GET, POST, PUT, DELETE)
class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['nombre_sede']
    ordering = ['nombre_sede']
    search_fields = ['nombre_sede', 'direccion']


# Crud de tabla Organizador (GET, POST, PUT, DELETE)
class OrganizadorViewSet(viewsets.ModelViewSet):
    queryset = Organizador.objects.all()
    serializer_class = OrganizadorSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['nombre']
    ordering = ['nombre']
    search_fields = ['nombre', 'correo', 'telefono']


# Crud de tabla Evento (GET, POST, PUT, DELETE)
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['nombre_evento', 'fecha_inicio', 'fecha_fin']
    ordering = ['nombre_evento']
    search_fields = ['nombre_evento', 'descripcion']


# Crud de tabla Asistente (GET, POST, PUT, DELETE)
class AsistenteViewSet(viewsets.ModelViewSet):
    queryset = Asistente.objects.all()
    serializer_class = AsistenteSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['nombre']
    ordering = ['nombre']
    search_fields = ['nombre', 'correo', 'telefono']


# Crud de tabla Inscripcion (GET, POST, PUT, DELETE)
class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['fecha_inscripcion']
    ordering = ['-fecha_inscripcion']


# Crud de tabla Pago (GET, POST, PUT, DELETE)
class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['monto', 'fecha_pago']
    ordering = ['-fecha_pago']


# Crud de tabla Conferencia (GET, POST, PUT, DELETE)
class ConferenciaViewSet(viewsets.ModelViewSet):
    queryset = Conferencia.objects.all()
    serializer_class = ConferenciaSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['titulo', 'hora_inicio']
    ordering = ['titulo']
    search_fields = ['titulo', 'descripcion']


# Crud de tabla Patrocinador (GET, POST, PUT, DELETE)
class PatrocinadorViewSet(viewsets.ModelViewSet):
    queryset = Patrocinador.objects.all()
    serializer_class = PatrocinadorSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['nombre']
    ordering = ['nombre']
    search_fields = ['nombre']