# test.py
from django.test import TestCase
from hotels.models import Hotel, City
from django.core.management import call_command
from io import StringIO
class ReaderTest(TestCase):
    def test_command_output(self):
        call_command('read')