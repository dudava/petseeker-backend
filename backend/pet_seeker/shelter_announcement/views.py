from . import serializers
from rest_framework.response import Response
from rest_framework import viewsets, mixins, generics, views
from .models import ShelterAnnouncement
from shelter.models import Shelter
from user.permissions import IsOwnerOrReadOnly, IsShelterOwnerOrReadOnly
from search_announcement.views import PageNumberPagination

class ShelterAnnouncementCreateEditViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ShelterAnnouncementDetailSerializer
    queryset = ShelterAnnouncement.objects.all()
    permission_classes = [IsOwnerOrReadOnly, IsShelterOwnerOrReadOnly]

class ShelterAnnouncementDeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
    permission_classes = [IsOwnerOrReadOnly, IsShelterOwnerOrReadOnly]
    
    def delete(self, request, pk, format=None):
        try:
            announcement = ShelterAnnouncement.objects.get(pk=pk)
        except ShelterAnnouncement.DoesNotExist:
            return Response({"error": "Объявление не существует"}, 400)
        announcement.delete()
        return Response({"success": "Объявление удалено"}, 200)
    

class ShelterAnnouncementDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = serializers.ShelterAnnouncementDetailSerializer

    def get(self, request, pk, format=None):
        try:
            announcement = ShelterAnnouncement.objects.get(pk=pk)
        except ShelterAnnouncement.DoesNotExist:
            return Response({"error": "Объявление не существует"}, 400)
        serializer = serializers.ShelterAnnouncementDetailSerializer(announcement)
        return Response(serializer.data, 200)
    

class ShelterListAnnouncementsView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = serializers.ShelterAnnouncementSerializer
    pagination_class = PageNumberPagination
    
    def get(self, request, pk, format=None):
        try:
            shelter = Shelter.objects.get(pk=pk)
        except Shelter.DoesNotExist:
            return Response({"error": "Приют не существует"}, 400)
        announcements = shelter.announcements.all()
        serializer = serializers.ShelterAnnouncementSerializer(announcements, many=True)
        response = serializer.data
        return Response(response, 200)