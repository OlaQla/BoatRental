from django.conf.urls import url, include
from .views import all_boats, boat_details

urlpatterns = [
    url(r'^$', all_boats, name='boats'),
    url(r'^(?P<boat_id>[0-9]+)$', boat_details, name="boat_details"),
]