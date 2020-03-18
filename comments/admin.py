from django.contrib import admin
from .models import Comment

# Register comments in admin panel
admin.site.register(Comment)