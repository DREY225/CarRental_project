from django.db import models
from CarMark.models import CarMark
# Create your models here.

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    mark = models.ForeignKey(CarMark, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = "Modèle"
        verbose_name_plural = "Modèles"

    def __str__(self):
        return f"{self.name}"