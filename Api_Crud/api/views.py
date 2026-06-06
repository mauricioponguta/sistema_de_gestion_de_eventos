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


# Clase base para auditoría
class AuditoriaViewSet(viewsets.ModelViewSet):

    def perform_create(self, serializer):
        usuario = self.request.data.get('usuario_creacion')

        serializer.save(
            usuario_creacion=usuario,
            usuario_modificacion=usuario
        )

    def perform_update(self, serializer):
        usuario = self.request.data.get('usuario_modificacion')

        serializer.save(
            usuario_modificacion=usuario
        )


# Crud de tabla Sede (GET, POST, PUT, DELETE)
class SedeViewSet(AuditoriaViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['nombre', 'ciudad', 'capacidad', 'fecha_creacion']
    ordering = ['nombre']
    search_fields = ['nombre', 'direccion', 'ciudad', 'email']


# Crud de tabla Organizador (GET, POST, PUT, DELETE)
class OrganizadorViewSet(AuditoriaViewSet):
    queryset = Organizador.objects.all()
    serializer_class = OrganizadorSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['nombre', 'apellido', 'empresa', 'fecha_creacion']
    ordering = ['nombre']
    search_fields = ['nombre', 'apellido', 'email', 'empresa']


# Crud de tabla Evento (GET, POST, PUT, DELETE)
class EventoViewSet(AuditoriaViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'capacidad_maxima']
    ordering = ['nombre']
    search_fields = ['nombre', 'descripcion']


# Crud de tabla Asistente (GET, POST, PUT, DELETE)
class AsistenteViewSet(AuditoriaViewSet):
    queryset = Asistente.objects.all()
    serializer_class = AsistenteSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['nombre', 'apellido', 'fecha_creacion']
    ordering = ['nombre']
    search_fields = ['nombre', 'apellido', 'email', 'documento_identidad']


# Crud de tabla Inscripcion (GET, POST, PUT, DELETE)
class InscripcionViewSet(AuditoriaViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['fecha_creacion', 'estado']
    ordering = ['-fecha_creacion']
    search_fields = ['estado']


# Crud de tabla Pago (GET, POST, PUT, DELETE)
class PagoViewSet(AuditoriaViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['monto', 'fecha_creacion', 'estado']
    ordering = ['-fecha_creacion']
    search_fields = ['estado', 'metodo_pago', 'referencia']


# Crud de tabla Conferencia (GET, POST, PUT, DELETE)
class ConferenciaViewSet(AuditoriaViewSet):
    queryset = Conferencia.objects.all()
    serializer_class = ConferenciaSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['titulo', 'fecha_hora_inicio', 'duracion_minutos']
    ordering = ['titulo']
    search_fields = ['titulo', 'descripcion', 'ponente', 'sala']


# Crud de tabla Patrocinador (GET, POST, PUT, DELETE)
class PatrocinadorViewSet(AuditoriaViewSet):
    queryset = Patrocinador.objects.all()
    serializer_class = PatrocinadorSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['nombre', 'nivel', 'monto_aporte', 'fecha_creacion']
    ordering = ['nombre']
    search_fields = ['nombre', 'contacto', 'email_contacto', 'nivel']