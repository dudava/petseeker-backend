from rest_framework import generics, views, viewsets, permissions, mixins
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from django.core import exceptions

from user_info.models import UserInfo
from shelter.models import Shelter
from . import models
from user_info.permissions import IsOwnerOrReadOnly, IsShelterOwnerByQueryParamsOrReadOnly, \
    IsShelterOwnerByAnnouncementQueryParamsOrReadOnly, IsPrivateAnnouncementOwnerByQueryParamsOrReadOnly
from . import serializers


class ProfileImageLoadView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = serializers.ProfileImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_info = self.request.user.user_info
        if not hasattr(user_info, 'profile_image'):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user_info=user_info)
        else:
            serializer = self.get_serializer(instance=user_info.profile_image, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({
            'success': 'Изображение успешно загружено',
        }, 200)


class ShelterImageLoadView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = serializers.ShelterImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated, IsShelterOwnerByQueryParamsOrReadOnly]

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


class PrivateAnnouncementImageLoadView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = serializers.PrivateAnnouncementImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated, IsPrivateAnnouncementOwnerByQueryParamsOrReadOnly]

    def post(self, request, pk, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            announcement = models.PrivateAnnouncement.objects.get(pk=pk)
        except models.PrivateAnnouncement.DoesNotExist:
            return Response({"error": "Объявление не существует"}, 400)
        images = serializer.validated_data.get('images')
        announcement_images = [models.PrivateAnnouncementImage(announcement=announcement, image=image) for image in images]
        models.PrivateAnnouncementImage.objects.bulk_create(announcement_images)
        return Response({
            'success': 'Изображения успешно загружены',
        }, 200)
    

class ShelterAnnouncementImageLoadView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = serializers.ShelterAnnouncementImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated, IsShelterOwnerByAnnouncementQueryParamsOrReadOnly]

    def post(self, request, pk, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            announcement = models.ShelterAnnouncement.objects.get(pk=pk)
        except models.ShelterAnnouncement.DoesNotExist:
            return Response({"error": "Объявление не существует"}, 400)
        images = serializer.validated_data.get('images')
        announcement_images = [models.ShelterAnnouncementImage(announcement=announcement, image=image) for image in images]
        models.ShelterAnnouncementImage.objects.bulk_create(announcement_images)
        return Response({
            'success': 'Изображения успешно загружены',
        }, 200)
    

class ProfileImageDeleteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user_info = self.request.user.user_info
        if user_info.profile_image:
            user_info.profile_image.delete()
        return Response({
            'success': 'Изображение успешно удалено',
        }, 200)


class ShelterImageDeleteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsShelterOwnerByQueryParamsOrReadOnly]

    def delete(self, request, pk, *args, **kwargs):
        try:
            image = models.ShelterImage.objects.get(pk=pk)
        except models.ShelterImage.DoesNotExist:
            return Response({"error": "Изображение не существует"}, 400)
        image.delete()
        return Response({
            'success': 'Изображение успешно удалено',
        }, 200)
    

class PrivateAnnouncementImageDeleteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsPrivateAnnouncementOwnerByQueryParamsOrReadOnly]

    def delete(self, request, pk, *args, **kwargs):
        try:
            image = models.PrivateAnnouncementImage.objects.get(pk=pk)
        except models.PrivateAnnouncementImage.DoesNotExist:
            return Response({"error": "Изображение не существует"}, 400)
        image.delete()
        return Response({
            'success': 'Изображение успешно удалено',
        }, 200)
    
    
class ShelterAnnouncementImageDeleteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsShelterOwnerByAnnouncementQueryParamsOrReadOnly]

    def delete(self, request, pk, *args, **kwargs):
        try:
            image = models.ShelterAnnouncementImage.objects.get(pk=pk)
        except models.ShelterAnnouncementImage.DoesNotExist:
            return Response({"error": "Изображение не существует"}, 400)
        image.delete()
        return Response({
            'success': 'Изображение успешно удалено',
        }, 200)