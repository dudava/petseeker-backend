from django.test import TestCase
from django.contrib.auth.models import User
from shelter.models import Shelter

from .services import YandexGeocoderCoordinatesToAddressServicer


class CommonGeocoderTest(TestCase):
    def test_get_address_from_coordinates(self):
        self.assertEqual(
            YandexGeocoderCoordinatesToAddressServicer.get_address_from_coordinates((55.101344, 73.350488)),
            'Россия, посёлок Омский, Центральная улица, 12Б'
        ) # my home 


class ShelterTest(TestCase):
    def test_create_shelter_with_incorrect_geo(self):
        user = User.objects.create_user(username="+123", password='123')
        shelter = Shelter.objects.create(user=user, name="ginger shelter", lattitude_longitude='55.101344, 73.350488')
        coordinates = YandexGeocoderCoordinatesToAddressServicer.long_latt_field_to_coordinates(shelter.lattitude_longitude)
        self.assertEqual(coordinates, (55.101344, 73.350488))
        address = YandexGeocoderCoordinatesToAddressServicer.get_address_from_coordinates(coordinates)
        self.assertEqual(address, 'Россия, посёлок Омский, Центральная улица, 12Б')