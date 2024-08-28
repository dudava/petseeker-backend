import random

from rest_framework import viewsets, mixins, views, permissions
from rest_framework.response import Response

from .models import PrivateAnnouncementFavourite, ShelterAnnouncementFavourite
from announcement.models import PrivateAnnouncement
from shelter_announcement.models import ShelterAnnouncement
from search_announcement.serializers import CommonAnnouncementListSerializer

class PrivateAnnouncementFavouriteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            announcement = PrivateAnnouncement.objects.get(pk=pk)
        except PrivateAnnouncement.DoesNotExist:
            return Response({'error': 'Объявление не существует'}, status=404)
        try:
            favourite = PrivateAnnouncementFavourite.objects.get(private_announcement=announcement, user=request.user)
        except PrivateAnnouncementFavourite.DoesNotExist:
            return Response({'error': 'Объявление не находится в избранном'}, status=404)                
        favourite.delete()
        return Response(status=200)

    def post(self, request, pk):
        try:
            announcement = PrivateAnnouncement.objects.get(pk=pk)
        except PrivateAnnouncement.DoesNotExist:
            return Response({'error': 'Объявление не существует'}, status=404)
        favourite_exists = PrivateAnnouncementFavourite.objects.filter(private_announcement=announcement, user=request.user).exists()
        if favourite_exists:
            return Response({'error': 'Объявление уже находится в избранном'}, status=409)
        else:
            PrivateAnnouncementFavourite.objects.create(
                user=request.user,
                private_announcement=announcement
            )
            return Response(status=201)


class ShelterAnnouncementFavouriteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            announcement = ShelterAnnouncement.objects.get(pk=pk)
        except ShelterAnnouncement.DoesNotExist:
            return Response({'error': 'Объявление не существует'}, status=404)
        try:
            favourite = ShelterAnnouncementFavourite.objects.get(shelter_announcement=announcement, user=request.user)
        except ShelterAnnouncementFavourite.DoesNotExist:
            return Response({'error': 'Объявление не находится в избранном'}, status=404)                
        favourite.delete()
        return Response(status=200)

    def post(self, request, pk):
        try:
            announcement = ShelterAnnouncement.objects.get(pk=pk)
        except ShelterAnnouncement.DoesNotExist:
            return Response({'error': 'Объявление не существует'}, status=404)
        favourite_exists = PrivateAnnouncementFavourite.objects.filter(announcement=announcement, user=request.user).exists()
        if favourite_exists:
            return Response({'error': 'Объявление уже находится в избранном'}, status=409)
        else:
            ShelterAnnouncementFavourite.objects.create(
                user=request.user,
                shelter_announcement=announcement
            )
            return Response(status=201)
    

class GetFavouritesView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        private_favourites = PrivateAnnouncementFavourite.objects.filter(user=request.user)
        private_announcements = [fav.private_announcement for fav in private_favourites]
        private_serializer = CommonAnnouncementListSerializer(private_announcements, many=True)

        shelter_favourites = ShelterAnnouncementFavourite.objects.filter(user=request.user)
        shelter_announcements = [fav.shelter_announcement for fav in shelter_favourites]
        shelter_serializer = CommonAnnouncementListSerializer(shelter_announcements, many=True)
        announcements = private_serializer.data + shelter_serializer.data
        random.shuffle(announcements)

        return Response(announcements, 200)
