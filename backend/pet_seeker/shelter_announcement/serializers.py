from rest_framework import serializers
from .models import ShelterAnnouncement

from announcement.serializers import PrivateAnnouncementSerializer

class ShelterAnnouncementDetailSerializer(serializers.ModelSerializer):
    lattitude_longitude = serializers.ReadOnlyField()
    class Meta:
        model = ShelterAnnouncement
        fields = '__all__'


class ShelterAnnouncementSerializer(serializers.ModelSerializer):
    shelter = serializers.ReadOnlyField(source='shelter.name')
    class Meta:
        model = ShelterAnnouncement
        fields = ('id', 'name', 'address', 'published_at', 'shelter')