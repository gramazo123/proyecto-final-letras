from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils import timezone
from .models import Cancione
from .models import Banda
from .forms import BandaForm
from .forms import CancionForm
from .forms import CancionBForm

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

def detalles_cancion(request, pk):
    post = get_object_or_404(Cancione, pk=pk)
    return render(request, 'letras/detalles_cancion.html', {'post': post})

def agregar_letras(request,pk):
    if request.method == "POST":
        form = CancionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.banda = Banda.objects.get(id = pk)
            post.save()
            return redirect('letras.views.detalles_cancion', pk=post.pk)
    else:
        form = CancionForm()
    return render(request, 'letras/agregar_letras.html', {'form': form})

def agregar_letrasb(request):
    if request.method == "POST":
        form = CancionBForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('letras.views.detalles_cancion', pk=post.pk)
    else:
        form = CancionBForm()
    return render(request, 'letras/agregar_letras.html', {'form': form})

def editar_cancion(request, pk):
    post = get_object_or_404(Cancione, pk=pk)
    if request.method == "POST":
        form = CancionForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('letras.views.detalles_cancion', pk=post.pk)
    else:
        form = CancionForm(instance=post)
    return render(request, 'letras/editar_cancion.html', {'form': form})

def eliminar_cancion(request, pk, pkb):
    Cancione.objects.get(pk=pk).delete()
    post = get_object_or_404(Banda, pk=pkb)
    return render(request, 'letras/detalles_banda.html', {'post': post})

