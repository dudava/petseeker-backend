from rest_framework import serializers
from . import models


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    is_shelter_owner = serializers.BooleanField() # в зависимости от значения, некоторые поля должны быть null
    contacts = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100) # для частника ФИО, для приюта название
    rating = serializers.ReadOnlyField()


class UserInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    name = serializers.CharField(max_length=100, required=False, allow_null=True)
    is_shelter_owner = serializers.BooleanField(required=False, allow_null=True)
    contacts = serializers.CharField(max_length=100, required=False, allow_null=True)
    rating = serializers.ReadOnlyField()

    class Meta:
        model = models.UserInfo
        fields = ('user_id', 'name', 'is_shelter_owner', 'contacts', 'rating')