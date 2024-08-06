from rest_framework import serializers
from .models import Shelter

class ShelterSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    lattitude_longitude = serializers.ReadOnlyField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Shelter
        fields = '__all__'

    def get_images(self, obj):
        return [{'id': image.id, 'url': image.image.url} for image in obj.images.all()]