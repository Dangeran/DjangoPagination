from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination import settings

BUS_STATIONS = []

with open(settings.BUS_STATION_CSV, newline='', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        BUS_STATIONS.append(row)

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(BUS_STATIONS, 10)
    page = paginator.page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
