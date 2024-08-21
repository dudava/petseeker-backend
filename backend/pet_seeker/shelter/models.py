from user_info.models import CustomUser
from django.core.exceptions import ValidationError
from django.db import models

from gis_app.model_mixins import LocationModelMixin

class Shelter(LocationModelMixin):
    user = models.ForeignKey(CustomUser, related_name='shelters', on_delete=models.CASCADE)
    inn = models.CharField(max_length=15)
    ogrn = models.CharField(max_length=15)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    contacts = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=100)
    registered_at = models.DateTimeField(auto_now_add=True)