from rest_framework import serializers
from . import models

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    is_shelter = serializers.BooleanField() # в зависимости от значения, некоторые поля должны быть null
    contacts = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100) # для частника ФИО, для приюта название
    location = serializers.CharField(max_length=200) # для частника район, для приюта полный адрес
    description = serializers.CharField(required=False, allow_null=True) # только для приютов (для частников null)
        

class UserInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    description = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = models.UserInfo
        fields = ('user_id', 'name', 'is_shelter', 'contacts', 'location', 'description')