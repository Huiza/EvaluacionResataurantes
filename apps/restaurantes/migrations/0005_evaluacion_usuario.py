# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-05-29 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0004_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantes.Usuario'),
        ),
    ]
