from django.contrib.auth.models import User
from . import models
from .serializers import UserSerializer

def create_user_with_userinfo(validated_data):
    user = User.objects.create_user(
            username=validated_data.get('phone_number'), 
            password=validated_data.get('password'),
        )
    user_info = models.UserInfo.objects.create(user=user)
    return user, user_info

def get_user_info(user : User):
    user_info = user.user_info
    data = {
        "id": user.id,
        "is_shelter": user_info.is_shelter,
        "username": user.username,
        "email": user.email,
        "name": user_info.name,
        "contacts": user_info.contacts,
        "location": user_info.location,
        "description": user_info.description,
    }
    return data