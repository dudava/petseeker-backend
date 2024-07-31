from rest_framework import serializers
from . import models

class ProfileImageSerializer(serializers.ModelSerializer): 
    image = serializers.ImageField()

    class Meta:
        model = models.ProfileImage
        fields = ('image', )


class ShelterImageSerializer(serializers.Serializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )
    class Meta:
        model = models.ShelterImage
        fields = ('images', )

class PrivateAnnouncementImageSerializer(serializers.Serializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )
    class Meta:
        model = models.PrivateAnnouncementImage
        fields = ('images', )


class ShelterAnnouncementImageSerializer(serializers.Serializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )
    class Meta:
        model = models.ShelterAnnouncementImage
        fields = ('images', )