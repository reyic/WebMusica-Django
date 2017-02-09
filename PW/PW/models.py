
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os
from django.db import models
from django.core.validators import RegexValidator
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.core.files import File  


# Create your models here.

class Usuario(models.Model):
	Nombre = models.CharField(max_length=30)
	Apellidos = models.CharField(max_length=30)
	User = models.CharField(max_length=20)
	Password = models.CharField(max_length=15)
	Direccion= models.CharField(max_length=30)
	CodigoPostal=models.CharField(max_length=5)
	Provincia=models.CharField(max_length=15)
	Email = models.EmailField()
	Dni= models.IntegerField(max_length=8)
	Visa = models.CharField(max_length=19, validators=[RegexValidator(regex='(((\d{4}-){3})|((\d{4} ){3}))\d{4}', message='Formato de Visa inválido', code='nomatch')])
	Observaciones=models.CharField(max_length=140)
	def __str__(self):
		return self.User


class Disco(models.Model):
	Genero = models.CharField(max_length=10)
	Titulo = models.CharField(max_length=40)
	Autor = models.CharField(max_length=40)
	Precio = models.CharField(max_length=8)
	imagen = models.FileField(blank=True,upload_to='/')
	cancion0 =models.FileField(blank=True,upload_to='/')
	cancion1 =models.FileField(blank=True,upload_to='/')
	cancion2 =models.FileField(blank=True,upload_to='/')
	cancion3 =models.FileField(blank=True,upload_to='/')
	cancion4 =models.FileField(blank=True,upload_to='/')
	cancion5 =models.FileField(blank=True,upload_to='/')
	cancion6 =models.FileField(blank=True,upload_to='/')
	cancion7 =models.FileField(blank=True,upload_to='/')
	cancion8 =models.FileField(blank=True,upload_to='/')
	cancion9 =models.FileField(blank=True,upload_to='/')
	