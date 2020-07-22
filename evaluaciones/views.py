from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from evaluaciones.serializers import EvaluacionSerializer
from evaluaciones.models import (
    Evaluacion,
    Pregunta,
    Respuesta,
    Curso,
)
from django.contrib.auth.models import User


class EvaluacionList(ListAPIView):
    serializer_class = EvaluacionSerializer
    queryset = Evaluacion.objects.all()


class EvaluacionRetrieve(RetrieveAPIView):
    serializer_class = EvaluacionSerializer
    queryset = Evaluacion.objects.all()


class CreateEvaluacionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        evaluacion_data = request.data
        preguntas = request.data['preguntas']

        # Get user object
        catedratico = User.objects.get(pk=evaluacion_data['catedratico'])
        # Get curso object
        curso = Curso.objects.get(pk=evaluacion_data['curso'])
        # Create evaluacion object
        evaluacion = Evaluacion.objects.create(
            titulo = evaluacion_data['titulo'],
            curso = curso,
            catedratico = catedratico
        )

        # Iterar sobre las preguntas para crear cada uno y luego sus respuestas
        for pregunta in preguntas:
            # Create pregunta object
            pregunta_object = Pregunta.objects.create(
                titulo = pregunta['titulo'],
                evaluacion = evaluacion
            )
            for respuesta in pregunta['respuestas']:
                Respuesta.objects.create(
                    titulo = respuesta['titulo'],
                    correcto = respuesta['correcto'],
                    pregunta = pregunta_object
                )
        serializer = EvaluacionSerializer(evaluacion)
        return Response(serializer.data)