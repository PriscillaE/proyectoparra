# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-02 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donaciones_Monetarias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Cantidad', models.IntegerField()),
                ('Forma_pago', models.CharField(choices=[('CH', 'Cheque'), ('DE', 'Deposito')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Donadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Donador_nombre', models.CharField(max_length=50)),
                ('Donador_correo', models.EmailField(max_length=254)),
                ('Donador_tel', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Historial_Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Diagnostico', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Paciente_nombre', models.CharField(max_length=30)),
                ('Paciente_apellido', models.CharField(max_length=30)),
                ('Paciente_edad', models.IntegerField()),
                ('Paciente_diagnostico', models.CharField(max_length=50)),
                ('Paciente_clinica', models.CharField(max_length=40)),
                ('Tutor_Padre', models.CharField(choices=[('RE', 'Remision'), ('TR', 'En Tratamiento'), ('DEP', 'Fallecido')], max_length=15)),
                ('Paciente_contacto', models.CharField(blank=True, max_length=15)),
                ('Estado_salud', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='historial_medico',
            name='Paciente_hm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Pacientes'),
        ),
        migrations.AddField(
            model_name='donaciones_monetarias',
            name='Donador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Donadores'),
        ),
    ]