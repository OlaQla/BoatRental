from django.conf.urls import url, include
from .views import all_boats

urlpatterns = [
    url(r'^$', all_boats, name='boats'),
]