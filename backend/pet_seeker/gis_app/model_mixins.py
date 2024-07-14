from django.db import models
from django.core.exceptions import ValidationError


class LocationModelMixin(models.Model):
    lattitude_longitude = models.CharField(max_length=100)
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.lattitude_longitude.strip():
            raise ValidationError("Поле долгота и широта не может быть пустым")

        try:
            latitude, longitude = self.lattitude_longitude.split(",")
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            raise ValidationError("Поле долгота и широта должно быть в формате 'широта,долгота'")

        if not -90 <= latitude <= 90:
            raise ValidationError("Широта должна быть в диапазоне от -90 до 90 градусов")   

        if not -180 <= longitude <= 180:
            raise ValidationError("Долгота должна быть в диапазоне от -180 до 180 градусов")
        super().save(*args, **kwargs)