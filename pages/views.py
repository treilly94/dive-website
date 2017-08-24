from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import json
import urllib.request
from django.utils import timezone

from .models import Location


class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'latest_location_list'

    def get_queryset(self):
        """
        Return the all locations alphabetically
        """
        return Location.objects.order_by('location_name')


class DetailView(generic.DetailView):
    model = Location
    template_name = 'pages/detail.html'

    def get_queryset(self):
        """
        Returns all location objects
        """
        return Location.objects


# def get_weather(request):
#     with urllib.request.urlopen("http://api.wunderground.com/api/740f0e4cc57ffebd/forecast10day/q/54.136801,-2.723933.json") as url:
#         weather = json.loads(url.read().decode())
#     return render(request, 'pages/detail.html', {'weather': weather})
