from user_info.models import CustomUser
from django.db import models
from django.core.exceptions import ValidationError
from announcement.models import PrivateAnnouncement

from .model_mixins import FeedbackModelMixin
from . import services

class UserFeedback(FeedbackModelMixin):
    user_by = models.ForeignKey(CustomUser, related_name='my_feedbacks', on_delete=models.CASCADE)
    user_to = models.ForeignKey(CustomUser, related_name='feedbacks', on_delete=models.CASCADE)
    announcement = models.ForeignKey(PrivateAnnouncement, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.user_by == self.user_to:
            raise ValidationError('Пользователь не может оставить отзыв сам на себя')

        super().save(*args, **kwargs)
        services.update_user_rating(self.user_to)