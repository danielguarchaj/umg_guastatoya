from django.urls import path, include
from rest_framework import routers

from evaluaciones.views import (
    EvaluacionList,
    EvaluacionRetrieve,
    CreateEvaluacionAPIView,
    CursoViewSet
)

app_name = 'evaluaciones'

router = routers.DefaultRouter()
router.register('cursos', CursoViewSet, basename='cursos')


urlpatterns = [
    path('', include(router.urls)),
    path('', EvaluacionList.as_view(), name='evaluaciones_list'),
    path('<int:pk>', EvaluacionRetrieve.as_view(), name='evaluaciones_list'),
    path('create/', CreateEvaluacionAPIView.as_view(), name='evaluacion_create'),
]