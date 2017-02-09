"""PW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from PW import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^login/', views.login, name='login'),
    url(r'^logout/',views.logout, name='logout'),
	url(r'^section/', views.mostrardisc, name='section'),
    url(r'^discos/$', views.mostrardisco, name='discos'),
    url(r'^registro/',views.registro,name='registro'),
    url(r'^settings/',views.settings,name='settings'),
    url(r'^mostrarperfil/$',views.mostrarperfil,name='mostrarperfil'),
    url(r'^editar/$',views.editar,name='editar'),
    url(r'^mostrardisc/$',views.mostrardisc,name='mostrardisc'),
    url(r'^comenta/$',views.comenta, name='comenta'),
    url(r'^registra_comentario/',views.registra_comentario,name='registra_comentario'),
    url(r'^admin/', admin.site.urls),
]

