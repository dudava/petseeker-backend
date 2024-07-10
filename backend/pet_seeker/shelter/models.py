from django.contrib.auth.models import User
from django.db import models

class Shelter(models.Model):
    user = models.ForeignKey(User, related_name='shelters', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
