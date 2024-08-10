from rest_framework import serializers
from . import models


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)
    contacts = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100) # для частника ФИО, для приюта название
    rating = serializers.ReadOnlyField()


class UserInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    name = serializers.CharField(max_length=100, required=False, allow_null=True)
    surname = serializers.CharField(max_length=100, required=False, allow_null=True)
    contacts = serializers.CharField(max_length=100, required=False, allow_null=True)
    rating = serializers.ReadOnlyField()

    class Meta:
        model = models.UserInfo
        fields = ('user_id', 'name', 'surname', 'contacts', 'rating')