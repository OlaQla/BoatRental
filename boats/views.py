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
from boats.forms import BoatSearchForm
from comments.models import Comment
from collections import namedtuple

# View of a comment for rendering to avoid having logic in templates
CommentView = namedtuple(
    'CommentView', [
        'commentText', 'date', 'username', 'stars', 'stars_missing'])

# View of boat availability for a day
Availability = namedtuple('Availability', ['day', 'in_month', 'available', 'before_today'])

# Search view, gets parameters from request queries, filters boats and returns filtered boat list view
def find_boats(request):

    # Get min cabins parameter, otherwise set to 0 which would ignore it
    request_min_cabins = request.GET.get("min_cabins")
    min_cabins = int(
        request_min_cabins) if request_min_cabins is not None and request_min_cabins is not '' else 0

    # Get min passangers parameter, otherwise set to 0 which would ignore it
    request_min_passangers = request.GET.get("min_passangers")
    min_passangers = int(
        request_min_passangers) if request_min_passangers is not None and request_min_passangers is not '' else 0

    # Get search name parameter, otherwise set to empty string which would ignore it
    request_search_name = request.GET.get("search_name")
    search_name = request_search_name if request_search_name is not None else ""

    # Get searched parameter to know if it's not the first search
    request_has_searched = request.GET.get("searched")
    has_searched = request_has_searched not in [None, '']

    """ Get boolean if sailboats should be included in result
        if not selected check if it is first search and set to opposite value to cater for
        having empty search string on first request but all checkboxes checked """
    request_include_sailboat = request.GET.get("include_sailboat")
    include_sailboat = bool(
        strtobool(request_include_sailboat)) if request_include_sailboat not in [
        None, ''] else not has_searched

    """ Get boolean if powerboats should be included in result
        if not selected check if it is first search and set to opposite value to cater for
        having empty search string on first request but all checkboxes checked """
    request_include_powerboat = request.GET.get("include_powerboat")
    include_powerboat = bool(
        strtobool(request_include_powerboat)) if request_include_powerboat not in [
        None, ''] else not has_searched

    """ Get boolean if catamarans should be included in result
        if not selected check if it is first search and set to opposite value to cater for
        having empty search string on first request but all checkboxes checked """
    request_include_catamaran = request.GET.get("include_catamaran")
    include_catamaran = bool(
        strtobool(request_include_catamaran)) if request_include_catamaran not in [
        None, ''] else not has_searched

    """ Get boolean if motoryachts should be included in result
        if not selected check if it is first search and set to opposite value to cater for
        having empty search string on first request but all checkboxes checked """
    request_include_motoryacht = request.GET.get("include_motoryacht")
    include_motoryacht = bool(
        strtobool(request_include_motoryacht)) if request_include_motoryacht not in [
        None, ''] else not has_searched

    # Get boats from database filtered by cabins, passangers and name
    boats = Boats.objects.all()
    boats = boats.filter(cabins__gte=min_cabins)
    boats = boats.filter(maxPassangers__gte=min_passangers)
    boats = boats.filter(model__icontains=search_name)

    # Pull boats and filter by checkboxes values
    boats = [boat for boat in list(boats) if
             (include_sailboat is True and boat.boatType == "sailboat") or
             (include_powerboat is True and boat.boatType == "powerboat") or
             (include_catamaran is True and boat.boatType == "sailing catamaran") or
             (include_motoryacht is True and boat.boatType == "motor yacht")]

    return render(
        request, "boats.html", {
            "boats": boats, "search_form": BoatSearchForm(
                initial=request.GET)})

# View of boat details
def boat_details(request, boat_id):

    # Pull boat from database
    boat = Boats.objects.get(id=boat_id)

    # Pull comments from database
    dbComments = Comment.objects.filter(boat__id=boat_id)

    # Convert comments to renderable view with calculations done to avoid having logic in templates
    comments = map(
        lambda c: CommentView(
            commentText=c.commentText,
            date=c.date,
            username=c.user.username,
            stars=range(
                c.starRating),
            stars_missing=range(
                5 - c.starRating)),
        dbComments)

    return render(
        request, "boat_details.html", {
            "boat": boat, "comments": comments})


""" Boat availability view, returns list of days filling full weeks for selected month. 
    Each day item consists of information indicating if selected boat is available, 
    if day is in selected month and number of the day. It is used to fill in calendar view in 
    boat details. 
"""
def boat_availability(request, boat_id, year, month):
    # Dictionary of days that the boat is already booked for in selected month
    daysTaken = {}

    # Gets start and end of month
    request_from_date = datetime(int(year), int(month) + 1, 1)
    request_to_date = datetime(
        int(year), int(month) + 1, calendar.monthrange(
            int(year), int(month) + 1)[1])

    # Load all selected boat order lines between selected dates
    orderDates = OrderLineItem.objects.filter(
        boat_id=boat_id).exclude(
        from_date__gte=request_to_date.timestamp()).exclude(
            to_date__lte=request_from_date.timestamp())

    # Mark days taken for all the orders (day sets union)
    for order in orderDates:
        startDate = date.fromtimestamp(order.from_date)
        endDate = date.fromtimestamp(order.to_date)

        # Mark all days that are within the order
        while startDate <= endDate:
            if startDate.month == int(month) + 1:
                daysTaken[startDate.day] = True
            startDate += timedelta(days=1)

    # Build a list of days making up full weeks for the month
    cal = calendar.Calendar()
    dayarray = []
    for day in cal.itermonthdates(int(year), int(month) + 1):
        dayarray.append(day)
    # Check availability with built daysTaken list, then convert availabilities to json response 
    return HttpResponse(
        json.dumps(
            list(
                map(
                    lambda d: (
                        Availability(
                            day=d.day,
                            in_month=d.month == int(month) + 1,
                            available=d.day not in daysTaken,
                            before_today=datetime(int(year), d.month, d.day).date() < datetime.now().date()))._asdict(),
                    dayarray))),
        content_type='application/json')
