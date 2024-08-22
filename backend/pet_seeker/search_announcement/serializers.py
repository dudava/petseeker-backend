from rest_framework import serializers


class CommonAnnouncementListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    pet_type = serializers.CharField(source='get_pet_type_display')
    breed = serializers.CharField()
    user = serializers.CharField(required=False, source='user.user_info.name')
    shelter = serializers.CharField(required=False, source='shelter.name')
    status = serializers.CharField(source='get_status_display')
    images = serializers.SerializerMethodField()
    name = serializers.CharField()
    published_at = serializers.CharField()
    address = serializers.CharField()

    def get_images(self, obj):
        return [image.image.url for image in obj.images.all()]

