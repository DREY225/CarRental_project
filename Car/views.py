from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Car
from .forms import CarForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car/index.html', {'cars': cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car/show.html', {'car': car})


def car_add(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Car:car_list'))  # Rediriger vers la liste des voitures après l'ajout réussi
    else:
        form = CarForm()
    return render(request, 'car/create.html', {'form': form})

@login_required
def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Car:car_list'))  # Redirige vers la liste des voitures après la modification
    else:
        form = CarForm(instance=car)
    return render(request, 'car/update.html', {'form': form})

@login_required
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'GET':
        car.delete()
        return HttpResponseRedirect(reverse('Car:car_list'))  # Redirige vers la liste des voitures après la suppression
    return HttpResponse("Méthode non autorisée", status=405)  # 405 est le code d'erreur "Méthode non autorisée"
