from django.conf import settings
import requests

class YandexGeocoderCoordinatesToAddressServicer:
    api_key = settings.YANDEXGEOCODER_API_KEY
    geocoder_url = 'https://geocode-maps.yandex.ru/1.x'

    @staticmethod
    def long_latt_field_to_coordinates(latt_long_field) -> tuple:
        latitude, longitude = latt_long_field.split(",")
        latitude = float(latitude)
        longitude = float(longitude)
        return (latitude, longitude)
    
    @classmethod
    def get_address_from_coordinates(self, coordinates: tuple):
        correct_format_cooridinates = ", ".join(tuple([str(coordinates[1]), str(coordinates[0])]))
         # не знаю как будет работать с приложением, но мне приходилось переворачивать координаты с яндекс карт
        response = requests.get(self.geocoder_url, params={
            'apikey': self.api_key,
            'geocode': correct_format_cooridinates,
            'results': 1,
            'format': 'json',
        })
        response.raise_for_status()
        result = (
            response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['formatted']
        )
        return result