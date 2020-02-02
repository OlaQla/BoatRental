from django.shortcuts import render
from django.utils import timezone
from .models import Boats

def all_boats(request):
    boats = Boats.objects.all()
    return render(request, "boats.html", {"boats": boats})

def boat_details(request, boat_id):
    boat = Boats.objects.get(id=boat_id)
    print(boat)
    return render(request, "boat_details.html", {"boat": boat})

