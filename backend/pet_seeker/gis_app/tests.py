from django.test import TestCase

from .services import YandexGeocoderCoordinatesToAddressServicer


class CommonGeocoderTest(TestCase):
    def test_get_address_from_coordinates(self):
        self.assertEqual(
            YandexGeocoderCoordinatesToAddressServicer.get_address_from_coordinates((55.101344, 73.350488)),
            'Россия, посёлок Омский, Центральная улица, 12Б'
        ) # my home 