from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class PrivateAnnouncementSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    lattitude_longitude = serializers.ReadOnlyField()
    class Meta:
        model = models.PrivateAnnouncement
        fields = '__all__'


class PrivateAnnouncementListSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()
    address = serializers.ReadOnlyField()
    published_at = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.user_info.name')
    status = serializers.ReadOnlyField()
    state = serializers.ReadOnlyField()

    class Meta:
        model = models.PrivateAnnouncement
        fields = ('name', 'address', 'published_at', 'user', 'status', 'state')


class UserAnnouncementSerializer(serializers.Serializer):
    is_shelter_owner = serializers.CharField(source='user_info.is_shelter_owner')
    name = serializers.CharField(source='user_info.name')
    contacts = serializers.CharField(source='user_info.contacts')
    date_joined = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'is_shelter_onwer', 'name', 'contacts', 'registered_at')


class PrivateAnnouncementDetailSerializer(serializers.Serializer):
    announcement_detail = PrivateAnnouncementSerializer()
    user = UserAnnouncementSerializer()