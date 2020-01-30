from django.shortcuts import render
from django.utils import timezone
from .models import Boats

def all_boats(request):
    boats = Boats.objects.all()
    return render(request, "boats.html", {"boats": boats})
