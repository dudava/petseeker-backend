from django.db import models
from django.contrib.auth.models import User

from shelter.models import Shelter
from .model_mixins import AnnouncementMixin

class PrivateAnnouncement(AnnouncementMixin):
    user = models.ForeignKey(User, related_name='announcements', on_delete=models.CASCADE)