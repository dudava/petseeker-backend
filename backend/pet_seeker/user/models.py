from django.contrib.auth.models import User
from django.db import models

class UserInfo(models.Model):
    user = models.OneToOneField(User, related_name='user_info', null=True, blank=True, on_delete=models.CASCADE)
    is_shelter = models.BooleanField() # в зависимости от значения, некоторые поля должны быть null
    contacts = models.CharField(max_length=100)
    name = models.CharField(max_length=100) # для частника ФИО, для приюта название
    location = models.CharField(max_length=200) # для частника район, для приюта полный адрес
    description = models.TextField(null=True, blank=True) # только для приютов (для частников null)