from django.db import models

from user.models import UserInfo
from shelter.models import Shelter


class ProfileImage(models.Model):
    user_info = models.OneToOneField(UserInfo, related_name='profile_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ShelterImage(models.Model):
    shelter = models.ForeignKey(Shelter, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shelter_images')
    uploaded_at = models.DateTimeField(auto_now_add=True)
