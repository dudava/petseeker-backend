from rest_framework import serializers


class CommonAnnouncementListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    pet_type = serializers.CharField()
    breed = serializers.CharField()
    color = serializers.CharField()
    user = serializers.CharField(required=False, source='user.user_info.name')
    shelter = serializers.CharField(required=False, source='shelter.name')
    images = serializers.SerializerMethodField()
    name = serializers.CharField()
    published_at = serializers.CharField()
    address = serializers.CharField()


    def get_images(self, obj):
        return [{'id': image.id, 'url': image.image.url} for image in obj.images.all()]
