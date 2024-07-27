from rest_framework import generics, views, viewsets, permissions, mixins
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from user.models import UserInfo
from shelter.models import Shelter
from . import models
from user.permissions import IsOwnerOrReadOnly, IsShelterOwnerOrReadOnly
from .serializers import ProfileImageSerializer, ShelterImageSerializer


class ProfileImageLoadView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = ProfileImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_info = self.request.user.user_info
        if user_info.profile_image:
            serializer = self.get_serializer(instance=user_info.profile_image, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user_info=user_info)
        return Response({
            'success': 'Изображение успешно загружено',
        }, 200)


class ShelterImageLoadView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = ShelterImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def post(self, request, pk, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            shelter = Shelter.objects.get(pk=pk)
        except Shelter.DoesNotExist:
            return Response({"error": "Приют не существует"}, 400)
        images = serializer.validated_data.get('images')
        shelter_images = [models.ShelterImage(shelter=shelter, image=image) for image in images]
        models.ShelterImage.objects.bulk_create(shelter_images)
        return Response({
            'success': 'Изображения успешно загружены',
        }, 200)


