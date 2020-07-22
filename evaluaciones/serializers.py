from rest_framework import serializers
from evaluaciones.models import (
    Curso,
    Evaluacion,
    Pregunta,
    Respuesta,
    EvaluacionResuelta,
    RespuestaSeleccionada
)

from users.serializers import UserProfileSerializer

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = '__all__'


class PreguntaSerializer(serializers.ModelSerializer):
    respuestas = RespuestaSerializer(many=True)
    class Meta:
        model = Pregunta
        fields = '__all__'


class EvaluacionSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True)
    catedratico = UserProfileSerializer()
    class Meta:
        model = Evaluacion
        fields = '__all__'
