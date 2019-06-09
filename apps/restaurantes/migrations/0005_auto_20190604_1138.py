# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-06-04 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0004_auto_20190603_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultado_indicador',
            name='id',
        ),
        migrations.AlterField(
            model_name='resultado_indicador',
            name='evaluacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, to='restaurantes.Evaluacion'),
        ),
        migrations.AlterField(
            model_name='resultado_indicador',
            name='indicador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='restaurantes.Indicador'),
        ),
    ]