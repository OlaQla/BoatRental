from django.db import models
from django.utils import timezone

class Boats(models.Model):
    model = models.CharField(max_length=254, default='')
    boatType = models.CharField(max_length=30, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    maxPassangers = models.DecimalField(max_digits=2, decimal_places=0)
    cabins = models.DecimalField(max_digits=2, decimal_places=0)
    lenght = models.DecimalField(max_digits=6, decimal_places=2)
    builtDate = models.DateField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.model
