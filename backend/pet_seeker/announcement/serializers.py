from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class AnnouncementSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = models.Announcement
        fields = '__all__'


class UserAnnouncementSerializer(serializers.Serializer):
    is_shelter = serializers.CharField(source='user_info.is_shelter')
    name = serializers.CharField(source='user_info.name')
    contacts = serializers.CharField(source='user_info.contacts')
    date_joined = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'is_shelter', 'name', 'contacts', 'registered_at')


class AnnouncementDetailSerializer(serializers.Serializer):
    announcement_detail = AnnouncementSerializer()
    user = UserAnnouncementSerializer()