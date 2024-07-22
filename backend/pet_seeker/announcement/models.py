from django.db import models
from django.conf import settings

from shelter.models import Shelter
from .model_mixins import AnnouncementMixin

class PrivateAnnouncement(AnnouncementMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='announcements', on_delete=models.CASCADE)