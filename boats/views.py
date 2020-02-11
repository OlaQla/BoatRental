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

def all_boats(request):
    boats = Boats.objects.all()
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

