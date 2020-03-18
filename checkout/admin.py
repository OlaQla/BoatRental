from django.contrib import admin
from .models import Order
from .models import OrderLineItem

from django.contrib import admin
from .models import Order, OrderLineItem


# Models for admin panel 
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


# Register admin panel models for checkout
admin.site.register(Order, OrderAdmin)
