from rest_framework import serializers
from .models import ShelterAnnouncement


class ShelterAnnouncementDetailSerializer(serializers.ModelSerializer):
    lattitude_longitude = serializers.ReadOnlyField()
    images = serializers.SerializerMethodField()
    
    class Meta:
        model = ShelterAnnouncement
        fields = '__all__'

    def get_images(self, obj):
        return [image.image.url for image in obj.images.all()]
    

class ShelterAnnouncementSerializer(serializers.ModelSerializer):
    shelter = serializers.ReadOnlyField(source='shelter.name')
    
    class Meta:
        model = ShelterAnnouncement
        fields = ('id', 'name', 'address', 'published_at', 'shelter')
