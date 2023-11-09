from django import forms
from .models import CarModel 
class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'  
