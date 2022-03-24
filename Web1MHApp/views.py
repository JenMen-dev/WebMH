from django.shortcuts import render, HttpResponse



# Create your views here.

def home(request):

    return render(request, "Web1MHApp/Home.html")



def tienda(request):

    return render(request, "Web1MHApp/tienda.html")



def contacto(request):

    return render(request, "Web1MHApp/contacto.html")