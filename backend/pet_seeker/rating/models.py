from django.contrib.auth.models import User
from django.db import models
from announcement.models import PrivateAnnouncement

from .model_mixins import FeedbackModelMixin


class UserFeedback(FeedbackModelMixin):
    user_by = models.ForeignKey(User, related_name='my_feedbacks', on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='feedbacks', on_delete=models.CASCADE)
    announcement = models.ForeignKey(PrivateAnnouncement, on_delete=models.CASCADE)