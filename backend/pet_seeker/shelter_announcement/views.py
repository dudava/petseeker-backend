from . import serializers
from rest_framework.response import Response
from rest_framework import viewsets, mixins, generics, views
from .models import ShelterAnnouncement
from shelter.models import Shelter


class ShelterAnnouncementCreateEditViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ShelterAnnouncementSerializer
    queryset = ShelterAnnouncement.objects.all()


class ShelterAnnouncementDeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
    def delete(self, request, pk, format=None):
        try:
            announcement = ShelterAnnouncement.objects.get(pk=pk)
        except ShelterAnnouncement.DoesNotExist:
            return Response({"error": "Объявление не существует"}, 400)
        announcement.delete()
        return Response({"success": "Объявление удалено"}, 200)
    

class ShelterAnnouncementDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = serializers.ShelterAnnouncementSerializer

    def get(self, request, pk, format=None):
        try:
            announcement = ShelterAnnouncement.objects.get(pk=pk)
        except ShelterAnnouncement.DoesNotExist:
            return Response({"error": "Объявление не существует"}, 400)
        serializer = serializers.ShelterAnnouncementSerializer(announcement)
        return Response(serializer.data, 200)
    

class ShelterListAnnouncementsView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = serializers.ShelterAnnouncementSerializer

    def get(self, request, pk, format=None):
        try:
            shelter = Shelter.objects.get(pk=pk)
        except Shelter.DoesNotExist:
            return Response({"error": "Приют не существует"}, 400)
        announcements = shelter.announcements.all()
        serializer = serializers.ShelterAnnouncementSerializer(announcements, many=True)
        response = serializer.data
        return Response(response, 200)