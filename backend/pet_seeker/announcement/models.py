from django.db import models
from django.contrib.auth.models import User

from shelter.models import Shelter


class AnnouncementMixin(models.Model):
    class StatusChoices(models.TextChoices):
        active = "Активный"
        in_process = "В процессе усыновления"
        inactive = "Неактивный"

    class PetTypeChoices(models.TextChoices):
        dog = "Собака"
        cat = "Кошка"

    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # критерии поиска
    pet_type = models.CharField(choices=PetTypeChoices.choices, max_length=50, blank=True, null=True)
    breed = models.CharField(max_length=50, blank=True, null=True)
    age = models.PositiveIntegerField(blank=False, null=False)
    status = models.CharField(max_length=50, choices=StatusChoices.choices)
    color = models.CharField(max_length=50, null=False, blank=False)
    sterilization = models.BooleanField(null=True)
    is_health_issues = models.BooleanField()
    health_issues = models.CharField(max_length=200, blank=True, null=True)
    vaccinations = models.BooleanField(null=True)
    weigth = models.FloatField(null=False, blank=False)
    dimmensions = models.PositiveIntegerField(null=False, blank=False)
    temperament = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['-published_at']


class PrivateAnnouncement(AnnouncementMixin):
    user = models.ForeignKey(User, related_name='announcements', on_delete=models.CASCADE)

class ShelterAnnouncement(AnnouncementMixin):
    shelter = models.ForeignKey(Shelter, related_name='announcements', on_delete=models.CASCADE)