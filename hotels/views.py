# views.py

from django.shortcuts import render
from .models import City, Hotel


def list(response, name):
    ls = City.objects.get(name=str(name))
    city_list = []
    hotels = ls.hotel_set.all()
    hotel_list = []
    for hotel in hotels:
        hotel_list.append(hotel.name)
    for city in City.objects.all():
        city_list.append(city.name)
    # This view should render a list of the hotels requested from the home
    # view given a POST request for a city
    return render(response, "hotels/list.html", {"hotel_list": hotel_list, "name": name,
                                                 "city_list": city_list})


def home(response):
    ls = City.objects.all()
    city_list = []
    for city in ls:
        city_list.append(city.name)
    return render(response, "hotels/home.html", {"city_list": city_list})
