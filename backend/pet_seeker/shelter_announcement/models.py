from django.db import models

from shelter.models import Shelter
from announcement.model_mixins import AnnouncementMixin


class ShelterAnnouncement(AnnouncementMixin):
    shelter = models.ForeignKey(Shelter, related_name='announcements', on_delete=models.CASCADE)

    status = models.CharField(
        max_length=50, choices=AnnouncementMixin.StatusChoices.choices, default=AnnouncementMixin.StatusChoices.looking_home
    )
    address = models.CharField(max_length=100, blank=True, null=True)
    lattitude_longitude = models.CharField(max_length=100, blank=True, null=True)
    contacts = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.contacts = self.shelter.telephone_number
        self.address = self.shelter.address
        self.status = AnnouncementMixin.StatusChoices.looking_home
        super().save(*args, **kwargs)
