from django.db import models
from django.contrib.auth.models import User


class Announcement(models.Model):
    user = models.ForeignKey(User, related_name='announcements', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

