
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from gis_app.model_mixins import LocationModelMixin


class AnnouncementMixin(LocationModelMixin):
    class StatusChoices(models.TextChoices):
        find = 'Нашел'
        lost = 'Потерял'
        looking_home = 'Ищет дом'

    class StateChoices(models.TextChoices):
        active = "Активный"
        in_process = "В процессе усыновления"
        inactive = "Неактивный"

    class PetTypeChoices(models.TextChoices):
        dog = "Собака"
        cat = "Кошка"

    name = models.CharField(max_length=100)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contacts = models.CharField(max_length=100)
    # критерии поиска
    pet_type = models.CharField(choices=PetTypeChoices.choices, max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, choices=StateChoices.choices, default=StateChoices.active)
    status = models.CharField(max_length=50, choices=StatusChoices.choices)
    breed = models.CharField(max_length=50, blank=True, null=True)
    age = models.PositiveIntegerField(blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(50)])
    gender = models.BooleanField() # True - male, False - female
    wool_type = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, null=False, blank=False)
    sterilization = models.BooleanField(null=True)
    allergenicity = models.BooleanField(null=True)
    health_issues = models.CharField(max_length=200, blank=True, null=True)
    vaccinations = models.BooleanField(null=True)
    weigth = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(150)])
    dimmensions = models.PositiveIntegerField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(200)])
    temperament = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['-published_at']

    