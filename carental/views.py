from django.shortcuts import render, get_object_or_404, redirect
from Car.models import Car

# Create your views here.

def accueil(request):
    cars = Car.objects.all()[:5]
    return render(request, 'home.html', {'Cars': cars})


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car/index.html', {'cars': cars})


