from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Banda

def lista_letras(request):
    posts = Banda.objects.all()
    return render(request, 'letras/lista_letras.html', {'posts': posts})

def detalles_banda(request, pk):
    post = get_object_or_404(Banda, pk=pk)
    return render(request, 'letras/detalles_banda.html', {'post': post})
