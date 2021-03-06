from django.db import models
from django.utils import timezone

""" Model representing a boat for rent """


class Boats(models.Model):
    model = models.CharField(max_length=254, default='')
    boatType = models.CharField(max_length=30, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    maxPassangers = models.DecimalField(max_digits=2, decimal_places=0)
    cabins = models.DecimalField(max_digits=2, decimal_places=0)
    lenght = models.DecimalField(max_digits=6, decimal_places=2)
    builtDate = models.DateField()
    image = models.ImageField(upload_to='images')

    # This is to avoid adding second s at the end in admin panel
    class Meta:
        verbose_name_plural = "Boats"

    def __str__(self):
        return self.model


""" An item in a list of featured boats for promotion, it is just a reference to one of the boats """


class FeaturedBoat(models.Model):
    boat = models.ForeignKey(Boats, on_delete=models.CASCADE)

    def __str__(self):
        return self.boat.model
