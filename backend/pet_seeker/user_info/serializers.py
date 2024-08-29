from rest_framework import serializers
from . import models


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)
    # contacts = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)  # для частника ФИО, для приюта название
    rating = serializers.ReadOnlyField()


class UserInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    phone_number = serializers.CharField(source='user.phone_number', required=False)
    name = serializers.CharField(max_length=100, required=False, allow_null=True)
    surname = serializers.CharField(max_length=100, required=False, allow_null=True)
    patronymic = serializers.CharField(max_length=100, required=False, allow_null=True)
    telegram = serializers.CharField(max_length=100, required=False, allow_null=True)
    gender = serializers.BooleanField(required=False, allow_null=True)
    rating = serializers.ReadOnlyField()

    class Meta:
        model = models.UserInfo
        fields = ('user_id', 'phone_number', 'name', 'surname', 'patronymic', 'gender', 'telegram', 'rating')

    def update(self, instance, validated_data):
        # Обновляем телефонный номер пользователя
        user_data = validated_data.pop('user', None)
        if user_data:
            user_instance = instance.user
            user_instance.phone_number = user_data.get('phone_number', user_instance.phone_number)
            user_instance.save()

        # Обновляем данные модели UserInfo
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance