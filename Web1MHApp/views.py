from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return HttpResponse("Home")

def tratamientos(request):

    return HttpResponse("Tratamientos")

def productos(request):

    return HttpResponse("Productos")

def calendario(request):

    return HttpResponse("Calendario")

def blog(request):

    return HttpResponse("Blog")

def contacto(request):

    return HttpResponse("Contacto")