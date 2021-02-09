from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import urllib.request
import urllib.parse

import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    data_from_csv = []
    with open('data-398-2018-08-30.csv', encoding='cp1251', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_from_csv.append(row)
    paginator = Paginator(data_from_csv, 10)
    current_page = request.GET.get('page', 1)
    stations_list = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if stations_list.has_previous():
        prev_page = stations_list.previous_page_number()
    if stations_list.has_next():
        next_page = stations_list.next_page_number()
    next_url = reverse('bus_stations') + '?' + urllib.parse.urlencode({'page': next_page})
    prev_url = reverse('bus_stations') + '?' + urllib.parse.urlencode({'page': prev_page})
    context = {
            'bus_stations': stations_list,
            'current_page': current_page,
            'prev_page_url': prev_url,
            'next_page_url': next_url,
        }
    return render(request, 'index.html', context=context)
