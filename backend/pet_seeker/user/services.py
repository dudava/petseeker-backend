from . import models
from .serializers import UserSerializer

def create_user_with_userinfo(validated_data):
    user = models.CustomUser.objects.create_user(
            phone_number=validated_data.get('phone_number'), 
        )
    user_info = models.UserInfo.objects.create(user=user)
    return user, user_info

def get_user_info(user : models.CustomUser):
    user_info = user.user_info
    data = {
        "id": user.id,
        "is_shelter_owner": user_info.is_shelter_owner,
        "phone_number": user.phone_number,
        "name": user_info.name,
        "contacts": user_info.contacts,
        'rating': user_info.rating,
        'profile_image': user_info.profile_image.image.url if user_info.profile_image else None,
    }
    return data