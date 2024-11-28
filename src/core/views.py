from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import Context, Template

def saludar(request):
	return HttpResponse("Rompan todooooooooooo!")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1> Esto tiene todo el sentido del mundo? <h1/>")

def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre}")

def index(request):
    return render(request, "core/index.html")