from django.db import models
from boats.models import Boats
from django.contrib.auth.models import User


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    """Summary of the order"""

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    user = models.ForeignKey(User, null=False)
    order = models.ForeignKey(Order, null=False)
    boat = models.ForeignKey(Boats, null=False)
    quantity = models.IntegerField(blank=False)
    from_date = models.IntegerField(blank=False)
    to_date = models.IntegerField(blank=False)
    subtotal = models.IntegerField()

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.boat.model, self.boat.price)
