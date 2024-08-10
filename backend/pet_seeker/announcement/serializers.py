from django.contrib.auth.models import User
from rest_framework import serializers
from . import models
from . import serializer_fields


class PrivateAnnouncementListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.user_info.name')
    images = serializers.SerializerMethodField()
    
    # надо бы как-нибудь поюзать
    class Meta:
        model = models.PrivateAnnouncement
        fields = ('id', 'name', 'images', 'address', 'published_at', 'user', 'status', 'state')

    def get_images(self, obj):
        return [{'id': image.id, 'url': image.image.url} for image in obj.images.all()]


class PrivateAnnouncementDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    lattitude_longitude = serializers.ReadOnlyField()
    images = serializers.SerializerMethodField()
    status = serializers.CharField(source='get_status_display')
    state = serializers.CharField(source='get_state_display')
    pet_type = serializers.CharField(source='get_pet_type_display')
    
    class Meta:
        model = models.PrivateAnnouncement
        fields = '__all__'
    
    def get_images(self, obj):
        return [{'id': image.id, 'url': image.image.url} for image in obj.images.all()]

    
class UserAnnouncementSerializer(serializers.Serializer):
    name = serializers.CharField(source='user_info.name')
    contacts = serializers.CharField(source='user_info.contacts')
    date_joined = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'is_shelter_onwer', 'name', 'contacts', 'registered_at')


class PrivateAnnouncementPresentationSerializer(serializers.Serializer):
    announcement_detail = PrivateAnnouncementDetailSerializer()
    user = UserAnnouncementSerializer()