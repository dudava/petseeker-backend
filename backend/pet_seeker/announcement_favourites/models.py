from django.db import models

from user_info.models import CustomUser
from announcement.models import PrivateAnnouncement
from shelter_announcement.models import ShelterAnnouncement


class PrivateAnnouncementFavourite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    private_announcement = models.ForeignKey(PrivateAnnouncement, on_delete=models.CASCADE)


class ShelterAnnouncementFavourite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shelter_announcement = models.ForeignKey(ShelterAnnouncement, on_delete=models.CASCADE)
