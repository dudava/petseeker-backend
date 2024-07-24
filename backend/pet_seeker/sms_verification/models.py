from django.db import models
from user.models import CustomUser


class SMSVerificationCode(models.Model):
    phone_number = models.CharField(max_length=10)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']