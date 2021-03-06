# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 11:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellidos', models.CharField(max_length=30)),
                ('User', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=15)),
                ('Direccion', models.CharField(max_length=30)),
                ('CodigoPostal', models.CharField(max_length=5)),
                ('Provincia', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('Dni', models.IntegerField(max_length=8)),
                ('Visa', models.CharField(max_length=19, validators=[django.core.validators.RegexValidator(code='nomatch', message='Formato de Visa inv\xe1lido', regex='(((\\d{4}-){3})|((\\d{4} ){3}))\\d{4}')])),
                ('Observaciones', models.CharField(max_length=140)),
            ],
        ),
    ]
