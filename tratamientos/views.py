from django.shortcuts import render
from tratamientos.models import Tratamiento

# Create your views here.

def tratamientos(request):

    tratamientos=Tratamiento.objects.all()
    return render(request, "tratamientos/tratamientos.html", {"tratamientos":tratamientos})