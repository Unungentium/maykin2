from django.core.management.base import BaseCommand, CommandError
from hotels.models import Hotel, City
import requests
import csv


class Command(BaseCommand):
    help = "Reads CSV files from the given website, decodes them saves them as hotel and city respectively"

    def handle(self, *args, **options):
        hotel_csv = 'http://rachel.maykinmedia.nl/djangocase/hotel.csv'
        city_csv = 'http://rachel.maykinmedia.nl/djangocase/city.csv'
        user, password = ('python-demo', 'claw30_bumps')
        hotel_download = requests.Session().get(
            url=hotel_csv, auth=(user, password)).content.decode('utf-8')
        city_download = requests.Session().get(
            url=city_csv, auth=(user, password)).content.decode('utf-8')
        hotel_list = list(csv.reader(
            hotel_download.splitlines(), delimiter=';'))
        city_list = list(csv.reader(
            city_download.splitlines(), delimiter=';'))
        unique_list = []
        for city in city_list:
            local = City.objects.create(name=city[1])
            local.save()
            for hotel in hotel_list:
                if city[0] == hotel[0]:
                    # some hotels in Bangkok are non-unique. Please fix the CSV files.
                    if hotel[2] not in unique_list:
                        unique_list.append(hotel[2])
                        local.hotel_set.create(name=hotel[2])
                        local.save()
