from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from gis_app.model_mixins import LocationModelMixin


class AnnouncementMixin(LocationModelMixin):
    class StatusChoices(models.TextChoices):
        find = 'find', 'find'
        lost = 'lost', 'lost'
        looking_home = 'looking_home', 'looking_home'
        give = 'give', 'give'

    class StateChoices(models.TextChoices):
        active = "active", "active"
        in_process = "in_process", "in_process"
        inactive = "inactive", "inactive"

    class PetTypeChoices(models.TextChoices):
        dog = "dog", "dog"
        cat = "cat", "cat"

    class AgeCategoryChoices(models.TextChoices):
        small = "small", "small"
        young = "young", "young"
        adult = "adult", "adult"
        old = "old", "old"
        unknown = "unknown", "unknown"

    class DimensionChoices(models.TextChoices):
        thin = "thin", "thin"
        average = "average", "average"
        full = "full", "full"

    class WoolTypeChoices(models.TextChoices):
        short = "short", "short"
        long = "long", "long"
        fluffy = "fluffy", "fluffy"
        tough = "tough", "tough"
        hairless = "hairless", "hairless"

    name = models.CharField(max_length=100)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contacts = models.CharField(max_length=100)
    # критерии поиска
    pet_type = models.CharField(max_length=50, blank=True, null=True, choices=PetTypeChoices.choices)
    state = models.CharField(max_length=50, choices=StateChoices.choices)
    status = models.CharField(max_length=50, choices=StatusChoices.choices)
    breed = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=50, blank=False, null=False, choices=AgeCategoryChoices.choices)
    gender = models.BooleanField()  # True - male, False - female
    wool_type = models.CharField(max_length=50, blank=True, null=True, choices=WoolTypeChoices.choices)
    sterilization = models.BooleanField(null=True)
    allergenicity = models.BooleanField(null=True)
    health_issues = models.BooleanField(null=True)
    vaccinations = models.BooleanField(null=True)
    weigth = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(150)])
    dimensions = models.CharField(max_length=50, null=False, blank=False, choices=DimensionChoices.choices,)
    temperament = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['-published_at']
