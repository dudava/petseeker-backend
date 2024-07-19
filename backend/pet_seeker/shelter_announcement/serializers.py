from rest_framework import serializers
from .models import ShelterAnnouncement


class ShelterAnnouncementSerializer(serializers.ModelSerializer):
    lattitude_longitude = serializers.ReadOnlyField()
    class Meta:
        model = ShelterAnnouncement
        fields = '__all__'
