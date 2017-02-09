import os 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *

from django import forms

from django.core.files import File  
from pymongo import MongoClient

from PW import forms 

import time
import datetime

from django.http import JsonResponse

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.tiendamusica

users=db['users']
discos=db['discos']
comentarios=db['comentarios']

# Create your views here.

def index(request):
	data=listadisco_index()
	return render(request,'index.html',{'form_log':LoginForm(),'index':listadisco_index()})

def section(request):
	return render(request,'section.html',{'form_log':LoginForm()})

def discos(request):
	return render(request, 'discos.html',{'form_log':LoginForm(),'infod':listardiscosgenero(disco), 'listadisc':listadisco()})

def login(request):
	if request.method=='POST':
		form_log = LoginForm(request.POST)
		x = db.users.find_one({"Usuario":request.POST['user']})
		if x!=None:
			if x[u'Password']==request.POST['password']:
				request.session['username']=request.POST['user']
				return render(request,'index.html', {'form_log':LoginForm(),'index':listadisco_index(), 'user' : request.session['username']})
			else:
				return render(request, 'index.html', {'form_log':LoginForm(),'index':listadisco_index()})
		else:
			return render(request, 'index.html', {'form_log':LoginForm(),'index':listadisco_index()})
	if 'username' in request.session:
		return render(request,'index.html',{'form_log':LoginForm(),'index':listadisco_index()})
	return render(request,'index.html',{'form_log':LoginForm(),'index':listadisco_index()})

def logout(request):
	if 'username' in request.session:
		del request.session['username']
	return HttpResponseRedirect('/')


def registro(request):
	if request.method=='POST':
		form_reg=RegForm(request.POST)
		if form_reg.is_valid():
			x=db.users.find_one({"User": request.POST['User']})
			if x==None:
				request.session["username"]=request.POST['User']
				db.users.insert({
					"Nombre": request.POST['Nombre'],
					"Apellidos": request.POST['Apellidos'],
					"Usuario": request.POST['User'],
					"Password": request.POST['Password'],
					"Direccion":request.POST['Direccion'],
					"CodigoPostal":request.POST['CodigoPostal'],
					"Provincia":request.POST['Provincia'],
					"Email": request.POST['Email'],
					"Dni": request.POST['Dni'],
					"Visa": request.POST['Visa'],
					"Observaciones":request.POST['Observaciones'],
					})
				return render(request, 'index.html',{'form_log' : LoginForm(), 'User' : request.session['username'], 'alert': 'El usuario se ha registrado','index':listadisco_index()})
		else:
			return render(request, 'registro.html', {'form_reg' : form_reg,'form_log' : LoginForm()})
	return render(request,'registro.html', {'form_reg':RegForm(),'form_log' : LoginForm()})

def mostrarperfil(request):
	perfil=request.GET.get('a',None)
	if perfil != None:
		x=db.users.find_one({"Usuario":perfil})
		if x!=None:
			datos=informacion_perfiles(perfil)
			if 'username' in request.session:
				return render(request,"infoperfil.html", {'info':datos, 'listausers':listaperfil()})
			else:
				return render(request,"index.html",{'form_log' : LoginForm(),'index':listadisco_index()})
	return render(request,'index.html',{'index':listadisco_index()})


def listaperfil():
	perfil=db.users.find({},{"_id": 0, "Nombre":1,"Apellidos":1,"Usuario":1,"Password":1,"Direccion":1,"CodigoPostal":1,"Provincia":1,"Email":1,"Dni":1,"Visa":1,"Observaciones":1})
	infoperfil=[]
	for doc in perfil:
		infoperfil.append(doc)
	return infoperfil


def informacion_perfiles(users):
	u=db.users.find_one({"Usuario":users})
	info=[]
	info.append(u[u'Nombre'])
	info.append(u[u'Apellidos'])
	info.append(u[u'Usuario'])
	info.append(u[u'Password'])
	info.append(u[u'Direccion'])
	info.append(u[u'CodigoPostal'])
	info.append(u[u'Provincia'])
	info.append(u[u'Email'])
	info.append(u[u'Dni'])
	info.append(u[u'Visa'])
	info.append(u[u'Observaciones'])
	return info


def editar(request):
	if 'username' in request.session:
		info=informacion_perfiles(request.session['username'])
		if request.method=='POST':
			db.users.update(
				{"Usuario":info[2]},{
				"Nombre": request.POST['Nombre'],
				"Apellidos": request.POST['Apellidos'],
				"Usuario": info[2],
				"Password": request.POST['Password'],
				"Direccion":request.POST['Direccion'],
				"CodigoPostal":request.POST['CodigoPostal'],
				"Provincia":request.POST['Provincia'],
				"Email": request.POST['Email'],
				"Dni": request.POST['Dni'],
				"Visa": request.POST['Visa'],
				"Observaciones":request.POST['Observaciones'],
			})
			return render(request, 'infoperfil.html', {'form_reg':RegForm(),'form_log' : LoginForm(), 'usuario' : request.session['username'],'info' : informacion_perfiles(request.session['username'])})
		else:
			return render(request, 'editar.html', {'form_log' : LoginForm(),'form_reg':RegForm(), 'usuario' : request.session['username'], 'info' : info})
	else:
		return render(request, 'editar.html', {'form_log' : LoginForm(),'form_reg':RegForm(), 'usuario' : request.session['username'], 'info' : info})
	return render(request, 'index.html', {'form_log' : LoginForm(),'form_reg':RegForm(),'info':info, 'listausers':listaperfil(),'index':listadisco_index()})


#Registro de discos
def settings(request):
	if request.method=='POST':
		disc_form=DiscForm(request.POST,request.FILES)
		disco=db.discos.find_one({"Titulo":request.POST['Titulo']})
		if disco==None:
			
			url='/static/img/' + request.FILES['imagen'].name
			url2='/static/songs/'+request.FILES['cancion0'].name
			url3='/static/songs/'+request.FILES['cancion1'].name
			url4='/static/songs/'+request.FILES['cancion2'].name
			url5='/static/songs/'+request.FILES['cancion3'].name
			url6='/static/songs/'+request.FILES['cancion4'].name
			url7='/static/songs/'+request.FILES['cancion5'].name
			url8='/static/songs/'+request.FILES['cancion6'].namecomentario
			url9='/static/songs/'+request.FILES['cancion7'].name
			url10='/static/songs/'+request.FILES['cancion8'].name
			url11='/static/songs/'+request.FILES['cancion9'].name
			
			imagenes_discos(request)
			cancion0(request)
			cancion1(request)
			cancion2(request)
			cancion3(request)
			cancion4(request)
			cancion5(request)
			cancion6(request)
			cancion7(request)
			cancion8(request)
			cancion9(request)

			db.discos.insert({
				"Genero":request.POST['Genero'],
				"Titulo":request.POST['Titulo'],
				"Autor":request.POST['Autor'],
				"Precio":request.POST['Precio'],
				"Imagen":url,
				"Cancion1":url2,
				"Cancion2":url3,
				"Cancion3":url4,
				"Cancion4":url5,
				"Cancion5":url6,
				"Cancion6":url7,
				"Cancion7":url8,
				"Cancion8":url9,
				"Cancion9":url10,
				"Cancion10":url11,
			})
			return render(request,'index.html',{'index':listadisco_index()})
	if 'username' in request.session and request.session['username'] == 'admin':		
		return render(request,'settings.html',{'disc_form':DiscForm()})
	else:
		return HttpResponseRedirect('/')
#Listar disco por genero
def listardiscosgenero(disco):
	g=db.discos.find({"Genero":disco},{"_id": 0,"Genero":1,"Titulo":1,"Autor":1,"Precio":1,"Imagen":1,"Cancion1":1,"Cancion2":1,"Cancion3":1,"Cancion4":1,"Cancion5":1,"Cancion6":1,"Cancion7":1,"Cancion8":1,"Cancion9":1,"Cancion10":1})
	infodisc=[]
	for doc in g:
		infodisc.append(doc)
	return infodisc

def listardiscostitulo(disco):
	g=db.discos.find({"Titulo":disco},{"_id": 0,"Genero":1,"Titulo":1,"Autor":1,"Precio":1,"Imagen":1,"Cancion1":1,"Cancion2":1,"Cancion3":1,"Cancion4":1,"Cancion5":1,"Cancion6":1,"Cancion7":1,"Cancion8":1,"Cancion9":1,"Cancion10":1})
	disc=[]
	for doc in g:
		disc.append(doc)
	return disc

def listadisco():
	disc=db.discos.find({},{"_id": 0,"Genero":1,"Titulo":1,"Autor":1,"Precio":1,"Imagen":1,"Cancion1":1,"Cancion2":1,"Cancion3":1,"Cancion4":1,"Cancion5":1,"Cancion6":1,"Cancion7":1,"Cancion8":1,"Cancion9":1,"Cancion10":1})
	infodisc=[]
	for doc in disc:
		infodisc.append(doc)
	return infodisc

def listadisco_index():
	disc=db.discos.find({},{"_id": 0,"Titulo":1,"Imagen":1})
	infodisc=[]
	for doc in disc:
		infodisc.append(doc)
	return infodisc

#muestra el disco en funcion del genero:
def mostrardisc(request):
	disco=request.GET.get('g',None)
	if disco!=None:
		d=db.discos.find({"Genero":disco})
		if d!=None:
			datadisc=listardiscosgenero(disco)
			if 'username' in request.session:
				return render(request,"section.html",{'infod':listardiscosgenero(disco), 'listadisc':listadisco()})
			else:
				return render(request,"index.html",{'form_log':LoginForm(),'index':listadisco_index()})
	return render(request,"index.html",{'form_log':LoginForm(),'index':listadisco_index()})

#Muestra el disco en funcion del titulo y comentarios

def mostrardisco(request):
	disco1=request.GET.get('d',None)
	if disco1!=None:
		d=db.discos.find({"Titulo":disco1})
		d=db.comentarios.find({"Disco":disco1})
		if d!=None:
			datadisc=listardiscostitulo(disco1)
			if 'username' in request.session:
				return render(request,"discos.html",{'comentario':listarCom(disco1),'disc':listardiscostitulo(disco1), 'listadisc':listadisco()})
			else:
				return render(request,"index.html",{'form_log':LoginForm(),'index':listadisco_index()})
	
	return render(request,"index.html",{'form_log':LoginForm(),'index':listadisco_index()})

#lista de comentarios por titulo:
def listacomentarios():
	g=db.comentarios.find({},{"_id": 0,"User":1,"Fecha":1,"Disco":1,"Comentario":1})
	disc=[]
	for doc in g:
		disc.append(doc)
	return disc

#lista comentarios por argumento:
def listarCom(disco):
	g=db.comentarios.find({"Disco":disco},{"_id": 0,"User":1,"Fecha":1,"Disco":1,"Comentario":1})
	disc=[]
	for doc in g:
		disc.append(doc)
	return disc


#Funcion donde le pasamos el disco y la fecha al formulario de
#registro de comentarios.
def comenta(request):
	x=datetime.datetime.now()
	com=request.GET.get('comentario',None)
	if com!=None:
		comentario=db.discos.find({"Titulo":com})
		if comentario!=None:
			datacom=listardiscostitulo(com)
			return render(request,'comentardisco.html',{'fecha':x.isoformat(),'y':listardiscostitulo(com)})

#Funcion hacer un comentario:
def registra_comentario(request):
	if request.method=='POST':
		db.comentarios.insert({
			"User": request.POST['user'],
			"Fecha": request.POST['fecha'],
			"Disco": request.POST['disco'],
			"Comentario":request.POST['comentario'],
			})
		return render(request,'comentardisco.html',{'listadisc':listadisco()})
	return render(request,"index.html",{'form_log':LoginForm(),'index':listadisco_index()})

#Funcion mostrar comentarios:



def imagenes_discos(request):
	directorio ='PW/static/img/'
	fichero = request.FILES['imagen']
	if not os.path.isdir(directorio):
		os.mkdir(directorio)
	with open(directorio + fichero.name,'wb+') as destination :
		for chunk in fichero.chunks():
			destination.write(chunk)

def cancion0(request):
	directorio='PW/static/songs/'
	fichero=request.FILES['cancion0']
	if not os.path.isdir(directorio):
		os.mkdir(directorio)
	with open(directorio+fichero.name,'wb+') as destination:
		for chunk in fichero.chunks():
			destination.write(chunk)

def cancion1(request):
	directorio='PW/static/songs/'
	fichero=request.FILES['cancion1']
	if not os.path.isdir(directorio):
		os.mkdir(directorio)
	with open(directorio+fichero.name,'wb+') as destination:
		for chunk in fichero.chunks():
			destination.write(chunk)


def cancion2(request):
	directorio='PW/static/songs/'
	fichero=request.FILES['cancion2']
	if not os.path.isdir(directorio):
		os.mkdir(directorio)
	with open(directorio+fichero.name,'wb+') as destination:
		for chunk in fichero.chunks():
			destination.write(chunk)


def cancion3(request):
	directorio='PW/static/songs/'
	fichero=request.FILES['cancion3']
	if not os.path.isdir(directorio):
		os.mkdir(directorio)
	with open(directorio+fichero.name,'wb+') as destination:
		for chunk in fichero.chunks():
			destination.write(chunk)


def cancion4(request):
	directorio='PW/static/songs/'
	fichero=request.FILES['cancion4']
	if not os.path.isdir(directorio):
		os.mkdir(directorio)
	with open(directorio+fichero.name,'wb+') as destination:
		for chunk in fichero.chunks():
			destination.write(chunk)

def cancion5(request):
	directorio='PW/static/songs/'
	fichero=request.FILES['cancion5']
	if not os.path.isdir(directorio):
		os.mkdir(directorio)
	with open(directorio+fichero.name,'wb+') as destination:
		for chunk in fichero.chunks():
			destination.write(chunk)

def cancion6(request):
	directorio='PW/static/songs/'
	fichero=request.FILES['cancion6']
	if not os.path.isdir(directorio):
		os.mkdir(directorio)
	with open(directorio+fichero.name,'wb+') as destination:
		for chunk in fichero.chunks():
			destination.write(chunk)


def cancion7(request):
	directorio='PW/static/songs/'
	fichero=request.FILES['cancion7']
	if not os.path.isdir(directorio):
		os.mkdir(directorio)
	with open(directorio+fichero.name,'wb+') as destination:
		for chunk in fichero.chunks():
			destination.write(chunk)


def cancion8(request):
	directorio='PW/static/songs/'
	fichero=request.FILES['cancion8']
	if not os.path.isdir(directorio):
		os.mkdir(directorio)
	with open(directorio+fichero.name,'wb+') as destination:
		for chunk in fichero.chunks():
			destination.write(chunk)


def cancion9(request):
	directorio='PW/static/songs/'
	fichero=request.FILES['cancion9']
	if not os.path.isdir(directorio):
		os.mkdir(directorio)
	with open(directorio+fichero.name,'wb+') as destination:
		for chunk in fichero.chunks():
			destination.write(chunk)