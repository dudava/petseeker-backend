from django.db import models

from shelter.models import Shelter
from announcement.model_mixins import AnnouncementMixin


class ShelterAnnouncement(AnnouncementMixin):
    shelter = models.ForeignKey(Shelter, related_name='announcements', on_delete=models.CASCADE)