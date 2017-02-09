from django import forms
from .models import *


class LoginForm(forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User', 'class' : 'log1'}))
	password = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Password', 'class' : 'log1', 'type' : 'password'}))

class RegForm(forms.ModelForm):
	class Meta:
		model = Usuario
		widgets = {
			'Nombre' : forms.TextInput(attrs={'placeholder': 'Nombre', 'class' : 'form-field'}),
			'Apellidos' : forms.TextInput(attrs={'placeholder': 'Apellidos', 'class' : 'form-field'}),
			'User' : forms.TextInput(attrs={'placeholder': 'User', 'name': 'User', 'class' : 'form-field'}),
			'Password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class' : 'form-field'}),
			'Direccion': forms.TextInput(attrs={'placeholder': 'Direccion', 'name': 'Direccion', 'class' : 'form-field'}),
			'CodigoPostal':forms.TextInput(attrs={'placeholder': 'CodigoPostal', 'name': 'CodigoPostal', 'class' : 'form-field'}),
			'Provincia':forms.TextInput(attrs={'placeholder': 'Provincia', 'name': 'Provincia', 'class' : 'form-field'}),
			'Email' : forms.TextInput(attrs={'placeholder': 'Email', 'class' : 'form-field'}),
			'Dni': forms.TextInput(attrs={'placeholder': 'DNI', 'class':'form-field'}),
			'Visa' : forms.TextInput(attrs={'placeholder': 'VISA', 'class' : 'form-field'}),
			'Observaciones':forms.Textarea(attrs={'placeholder': 'Observaciones', 'class':'form-field'}),
			}
		fields = ( 'Nombre', 'Apellidos', 'User', 'Password', 'Direccion','CodigoPostal','Provincia','Email','Dni','Visa','Observaciones')


class DiscForm(forms.ModelForm):
	class Meta:
		model=Disco 
		widgets={
			'Genero':forms.TextInput(attrs={'placeholder':'Genero','class' : 'form-field'}),
			'Titulo':forms.Textarea(attrs={'placeholder':'Titulo','class' : 'form-field'}),
			'Autor':forms.Textarea(attrs={'placeholder':'Autor','class' : 'form-field'}),
			'Precio':forms.Textarea(attrs={'placeholder':'Precio','class' : 'form-field'}),
			
			}
		fields = ('Genero','Titulo','Autor','Precio','imagen','cancion0','cancion1','cancion2','cancion3','cancion4','cancion5','cancion6','cancion7','cancion8','cancion9')