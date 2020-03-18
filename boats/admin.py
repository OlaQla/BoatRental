from django.contrib import admin
from .models import Boats, FeaturedBoat

# Register boats models in admin panel
admin.site.register(Boats)
admin.site.register(FeaturedBoat)