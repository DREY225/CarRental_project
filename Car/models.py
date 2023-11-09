from django.db import models
from CarMark.models import CarMark
from CarModel.models import CarModel
from django.contrib.humanize.templatetags.humanize import intcomma


# Create your models here.

class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    mark = models.ForeignKey(CarMark, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    class Meta:
        verbose_name = "Voiture"
        verbose_name_plural = "Voitures"
        
    def __str__(self):
        return f"{self.mark} - {self.model}"
    
    def formatted_price(self):
        return intcomma(int(self.price))
    