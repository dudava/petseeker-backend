from rest_framework import serializers


class AnnouncementFilterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    pet_type = serializers.CharField()
    breed = serializers.CharField()
    color = serializers.CharField()
    user = serializers.CharField(required=False, source='user.user_info.name')
    shelter = serializers.CharField(required=False, source='shelter.name')

