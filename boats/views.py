from django.shortcuts import render
from django.utils import timezone
from .models import Boats
from checkout.models import OrderLineItem
from django.http import HttpResponse
import calendar
from django.core.serializers import serialize
import json
from datetime import date, datetime, timedelta
from collections import namedtuple
from distutils.util import strtobool

def find_boats(request):
    request_min_cabins = request.GET.get("min_cabins")
    min_cabins = int(request_min_cabins) if request_min_cabins is not None and request_min_cabins is not '' else 0

    request_min_passangers = request.GET.get("min_passangers")
    min_passangers = int(request_min_passangers) if request_min_passangers is not None and request_min_passangers is not '' else 0

    request_search_name = request.GET.get("search_name")
    search_name = request_search_name if request_search_name is not None else ""

    request_include_sailboat = request.GET.get("include_sailboat")
    include_sailboat = bool(strtobool(request_include_sailboat)) if request_include_sailboat not in [None, ''] else True
    print(include_sailboat)
    print(request_include_sailboat)

    request_include_powerboat = request.GET.get("include_powerboat")
    include_powerboat = bool(strtobool(request_include_powerboat)) if request_include_powerboat is not None and not '' else True

    request_include_catamaran = request.GET.get("include_catamaran")
    include_catamaran = bool(strtobool(request_include_catamaran)) if request_include_catamaran is not None and not '' else True

    request_include_motoryacht = request.GET.get("include_motoryacht")
    include_motoryacht = bool(strtobool(request_include_motoryacht)) if request_include_motoryacht is not None and not '' else True

    boats = Boats.objects.all()
    boats = boats.filter(cabins__gte=min_cabins)
    boats = boats.filter(maxPassangers__gte=min_passangers)
    boats = boats.filter(model__icontains=search_name)
    
    boats = [boat for boat in list(boats) if \
        (include_sailboat is True and boat.boatType == "sailboat") or \
        (include_powerboat is True and boat.boatType == "powerboat") or \
        (include_catamaran is True and boat.boatType == "sailing catamaran") or \
        (include_motoryacht is True and boat.boatType == "motor yacht")]
    
    return render(request, "boats.html", {"boats": boats})

def boat_details(request, boat_id):
    boat = Boats.objects.get(id=boat_id)
    print(boat)
    return render(request, "boat_details.html", {"boat": boat})

def boat_availability(request, boat_id, year, month):
    daysTaken = {}
    request_from_date = datetime(int(year), int(month), 1)
    request_to_date = datetime(int(year), int(month), calendar.monthrange(int(year),int(month))[1])
    orderDates = OrderLineItem.objects.filter(boat_id=boat_id).exclude(from_date__gte=request_to_date.timestamp()).exclude(to_date__lte=request_from_date.timestamp())
    
    for order in orderDates: 
        startDate = date.fromtimestamp(order.from_date)
        endDate = date.fromtimestamp(order.to_date)
        while startDate <= endDate:
            if startDate.month == int(month): 
                daysTaken[startDate.day] = True 
            startDate += timedelta(days=1)      

    cal = calendar.Calendar()
    dayarray = []
    for day in cal.itermonthdates(int(year), int(month)):
	    dayarray.append(day)
    Availability = namedtuple('Availability', 'day in_month available')
    return HttpResponse(json.dumps(list(map(lambda d: (Availability(day=d.day, in_month=d.month == int(month), available=d.day not in daysTaken))._asdict(), dayarray))), content_type='application/json')

