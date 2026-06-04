from rest_framework import serializers

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

# Serializador para sedes
class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'


# Serializador para organizadores
class OrganizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizador
        fields = '__all__'


# Serializador para eventos
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


# Serializador para asistentes
class AsistenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistente
        fields = '__all__'


# Serializador para inscripciones
class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'


# Serializador para pagos
class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'


# Serializador para conferencias
class ConferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conferencia
        fields = '__all__'


# Serializador para patrocinadores
class PatrocinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patrocinador
        fields = '__all__'