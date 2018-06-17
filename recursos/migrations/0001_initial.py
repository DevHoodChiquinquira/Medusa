# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-06-17 02:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('espaciofisico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recursoTecnologico', models.BooleanField(default=True)),
                ('disponibilidad', models.BooleanField(default=False, verbose_name='Disponible')),
                ('estadoBaja', models.BooleanField(default=False, verbose_name='Baja de Activo')),
                ('descripcion', models.CharField(max_length=45, verbose_name='Descripci\xf3n')),
                ('caracteristicas', models.TextField(blank=True, null=True)),
                ('marca', models.CharField(blank=True, max_length=45, null=True)),
                ('modelo', models.CharField(blank=True, max_length=45, null=True)),
                ('numeroSerie', models.CharField(blank=True, max_length=45, null=True, verbose_name='N\xfamero de Serie')),
                ('accesorios', models.TextField(blank=True, null=True)),
                ('perifericos', models.TextField(blank=True, null=True, verbose_name='Perif\xe9ricos')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espaciofisico.Sede', verbose_name='Sede')),
            ],
        ),
    ]