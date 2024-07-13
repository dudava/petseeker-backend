from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from gis_app.models import LocationModelMixin

class Shelter(LocationModelMixin):
    user = models.ForeignKey(User, related_name='shelters', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()


    