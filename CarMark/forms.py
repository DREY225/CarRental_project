from django import forms
from .models import CarMark


class CarMarkForm(forms.ModelForm):
    class Meta:
        model = CarMark
        fields = '__all__'
