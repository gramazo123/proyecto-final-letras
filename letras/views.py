from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils import timezone
from .models import Banda
from .forms import BandaForm


def lista_letras(request):
    posts = Banda.objects.all()
    return render(request, 'letras/lista_letras.html', {'posts': posts})

def detalles_banda(request, pk):
    post = get_object_or_404(Banda, pk=pk)
    return render(request, 'letras/detalles_banda.html', {'post': post})

def agregar_banda(request):
    if request.method == "POST":
        form = BandaForm(request.POST, request.FILES)	
        if form.is_valid():                
            post = form.save(commit=False) 
            post.save()
            return redirect('letras.views.detalles_banda', pk=post.pk)
    else:
        form = BandaForm()
    return render(request, 'letras/agregar_banda.html', {'form': form})

def editar_banda(request, pk):
        post = get_object_or_404(Banda, pk=pk)
        if request.method == "POST":
            form = BandaForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)                
                post.save()
                return redirect('letras.views.detalles_banda', pk=post.pk)
        else:
            form = BandaForm(instance=post)
        return render(request, 'letras/editar_banda.html', {'form': form})
