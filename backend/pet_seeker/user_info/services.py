from . import models
from .serializers import UserSerializer

from image_loader.models import ProfileImage


def create_user_with_userinfo(validated_data):
    user = models.CustomUser.objects.create_user(
            phone_number=validated_data.get('phone_number'), 
        )
    user_info = models.UserInfo.objects.create(user=user)
    return user, user_info


def get_user_info(user: models.CustomUser):
    user_info = user.user_info
    data = {
        "id": user.id,
        "phone_number": user.phone_number,
        "name": user_info.name,
        "surname": user_info.surname,
        "patronymic": user_info.patronymic,
        "gender": user_info.gender,
        "telegram": user_info.telegram,
        'rating': user_info.rating,
        'date_joined': user.date_joined,
    }
    try:
        data['profile_image'] = user_info.profile_image.image.url
    except ProfileImage.DoesNotExist:
        data['profile_image'] = None
    return data