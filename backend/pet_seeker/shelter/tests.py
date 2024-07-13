from django.contrib.auth.models import User
from shelter.models import Shelter
from django.test import TestCase

class ShelterTest(TestCase):
    def test_create_shelter_with_incorrect_geo(self):
        user = User.objects.create_user(username="+123", password='123')
        shelter = Shelter.objects.create(user=user, name="ginger shelter", lattitude_longitude='55.102943, ')