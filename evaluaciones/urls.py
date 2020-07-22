from django.urls import path, include

from evaluaciones.views import (
    EvaluacionList,
    EvaluacionRetrieve,
    CreateEvaluacionAPIView,
)

app_name = 'evaluaciones'

urlpatterns = [
    path('', EvaluacionList.as_view(), name='evaluaciones_list'),
    path('<int:pk>', EvaluacionRetrieve.as_view(), name='evaluaciones_list'),
    path('create/', CreateEvaluacionAPIView.as_view(), name='evaluacion_create'),
]