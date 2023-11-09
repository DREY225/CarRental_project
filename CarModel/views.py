from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import CarModel
from .forms import CarModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def carmodel_list(request):
    carmodels = CarModel.objects.all()
    return render(request, 'carmodel/index.html', {'carmodels': carmodels})

def carmodel_detail(request, pk):
    carmodel = get_object_or_404(CarModel, pk=pk)
    return render(request, 'carmodel/show.html', {'carmodel': carmodel})

def carmodel_add(request):
    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('CarModel:carmodel_add')
    else:
        form = CarModelForm()
    return render(request, 'carmodel/create.html', {'form': form})
@login_required
def carmodel_edit(request, pk):
    carmodel = get_object_or_404(CarModel, pk=pk)
    if request.method == 'POST':
        form = CarModelForm(request.POST, instance=carmodel)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('CarModel:carmodel_list'))
    else:
        form = CarModelForm(instance=carmodel)
    return render(request, 'carmodel/update.html', {'form': form})
@login_required
def carmodel_delete(request, pk):
    carmodel = get_object_or_404(CarModel, pk=pk)
    if request.method == 'GET':
        carmodel.delete()
        return HttpResponseRedirect(reverse('CarModel:carmodel_list'))
    return HttpResponse("Méthode non autorisée", status=405)
