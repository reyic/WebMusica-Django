# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-14 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PW', '0005_auto_20160509_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='disco',
            name='cancion0',
            field=models.FileField(blank=True, upload_to='/'),
        ),
        migrations.AddField(
            model_name='disco',
            name='cancion1',
            field=models.FileField(blank=True, upload_to='/'),
        ),
        migrations.AddField(
            model_name='disco',
            name='cancion2',
            field=models.FileField(blank=True, upload_to='/'),
        ),
        migrations.AddField(
            model_name='disco',
            name='cancion3',
            field=models.FileField(blank=True, upload_to='/'),
        ),
        migrations.AddField(
            model_name='disco',
            name='cancion4',
            field=models.FileField(blank=True, upload_to='/'),
        ),
        migrations.AddField(
            model_name='disco',
            name='cancion5',
            field=models.FileField(blank=True, upload_to='/'),
        ),
        migrations.AddField(
            model_name='disco',
            name='cancion6',
            field=models.FileField(blank=True, upload_to='/'),
        ),
        migrations.AddField(
            model_name='disco',
            name='cancion7',
            field=models.FileField(blank=True, upload_to='/'),
        ),
        migrations.AddField(
            model_name='disco',
            name='cancion8',
            field=models.FileField(blank=True, upload_to='/'),
        ),
        migrations.AddField(
            model_name='disco',
            name='cancion9',
            field=models.FileField(blank=True, upload_to='/'),
        ),
        migrations.AlterField(
            model_name='disco',
            name='Autor',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='disco',
            name='Titulo',
            field=models.CharField(max_length=40),
        ),
    ]