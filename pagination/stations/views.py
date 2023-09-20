from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    num_page = int(request.GET.get('page', 1))

    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        new_dict = list(reader)

    page = Paginator(new_dict, 10)
    page = page.page(num_page)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
