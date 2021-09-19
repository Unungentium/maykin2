# models.py
from django.db import models


class City(models.Model):
    """City is the object that stores the city names"""
    name = models.CharField(
        max_length=300)  # length is kept at 300 to ensure the possibility of adding other cities with longer name

    def __str__(self):
        return self.name


class Hotel(models.Model):
    """Hotel is the object that stores hotel names with the attribute of city which stores the city in which the hotel is."""
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
