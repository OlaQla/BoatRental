from django.conf.urls import url, include
from .views import all_boats, boat_details, boat_availability

urlpatterns = [
    url(r'^$', all_boats, name='boats'),
    url(r'^(?P<boat_id>[0-9]+)$', boat_details, name="boat_details"),
    url(r'^availability/(?P<boat_id>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)$', boat_availability, name="boat_availability")
]