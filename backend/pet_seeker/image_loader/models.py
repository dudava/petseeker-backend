from django.db import models

from user_info.models import UserInfo
from shelter.models import Shelter
from announcement.models import PrivateAnnouncement
from shelter_announcement.models import ShelterAnnouncement


class ProfileImage(models.Model):
    user_info = models.OneToOneField(UserInfo, related_name='profile_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ShelterImage(models.Model):
    shelter = models.ForeignKey(Shelter, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shelter_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class PrivateAnnouncementImage(models.Model):
    announcement = models.ForeignKey(PrivateAnnouncement, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='announcement_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ShelterAnnouncementImage(models.Model):
    announcement = models.ForeignKey(ShelterAnnouncement, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='announcement_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)