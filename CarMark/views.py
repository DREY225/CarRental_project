from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import CarMark
from .forms import CarMarkForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def carmark_list(request):
    carmarks = CarMark.objects.all() 
    return render(request, 'carmark/index.html', {'carmarks': carmarks}) # carmarks est le nom de la variable qui sera utilisée dans le template

def carmark_detail(request, pk):
    carmark = get_object_or_404(CarMark, pk=pk)
    return render(request, 'carmark/show.html', {'carmark': carmark})

def carmark_add(request):
    if request.method == 'POST': 
        form = CarMarkForm(request.POST, request.FILES) # request.FILES pour les fichiers
        if form.is_valid():
            form.save() # enregistre les données dans la base de données
            return redirect('CarMark:carmark_add') # carmark_list est le nom de la vue défini dans urls.py
    else:
        form = CarMarkForm() # crée un formulaire vide
    return render(request, 'carmark/create.html', {'form': form}) # form est le nom de la variable qui sera utilisée dans le template

@login_required
def carmark_edit(request, pk):
    carmark = get_object_or_404(CarMark, pk=pk) # pk est la clé primaire de l'objet à modifier
    if request.method == 'GET':
        form = CarMarkForm(request.POST, instance=carmark) # instance permet de pré-remplir le formulaire avec les données de l'objet à modifier
        if form.is_valid():
            form.save()
            return redirect('CarMark:carmark_list') # carmark_list est le nom de la vue défini dans urls.py
    else:
        form = CarMarkForm(instance=carmark) # crée un formulaire pré-rempli avec les données de l'objet à modifier
    return render(request, 'carmark/update.html', {'form': form}) 

@login_required
def carmark_delete(request, pk): 
    carmark = get_object_or_404(CarMark, pk=pk) 
    if request.method == 'GET':
        carmark.delete()
        return HttpResponseRedirect(reverse('CarMark:carmark_list'))  # Redirige vers la liste des voitures après la suppression
    return HttpResponse("Méthode non autorisée", status=405)
