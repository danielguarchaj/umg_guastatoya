# Generated by Django 3.0.8 on 2020-07-22 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluaciones', '0002_auto_20200721_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='evaluacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='evaluaciones.Evaluacion'),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='evaluaciones.Pregunta'),
        ),
    ]
