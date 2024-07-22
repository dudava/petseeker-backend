from django.db import models
from user.models import CustomUser

from shelter.models import Shelter
from .model_mixins import AnnouncementMixin

class PrivateAnnouncement(AnnouncementMixin):
    user = models.ForeignKey(CustomUser, related_name='announcements', on_delete=models.CASCADE)