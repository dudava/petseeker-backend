from django.db import models
from django.core import validators

class FeedbackMixin(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    mark = models.IntegerField(validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(5),
    ])

    class Meta:
        abstract = True