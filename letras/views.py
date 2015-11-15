from django.shortcuts import render
from django.utils import timezone
from .models import Banda

def lista_letras(request):
    posts = Banda.objects.all()
    return render(request, 'letras/lista_letras.html', {'posts': posts})

