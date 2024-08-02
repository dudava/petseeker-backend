from django.contrib.auth.models import User
from rest_framework import generics, mixins, viewsets, permissions
from rest_framework.response import Response

from . import models, serializers
from user.permissions import IsOwnerOrReadOnly, IsPrivateAnnouncementOwnerByQueryParamsOrReadOnly

class PrivateAnnouncementCreateEditViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = models.PrivateAnnouncement.objects.all()
    serializer_class = serializers.PrivateAnnouncementDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PrivateAnnouncementDeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsPrivateAnnouncementOwnerByQueryParamsOrReadOnly]
    # TODO: защита от удаления не своих объявлений
    def delete(self, request, pk, format=None):
        try:
            announcement = models.PrivateAnnouncement.objects.get(pk=pk)
        except models.Announcement.DoesNotExist:
            return Response({"error": "Объявление не существует"}, 400)
        announcement.delete()
        return Response({"success": "Объявление удалено"}, 200)


class PrivateAnnouncementDetailView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.PrivateAnnouncement.objects.all()
    serializer_class = serializers.PrivateAnnouncementDetailSerializer


class PrivateAnnouncementPresentationView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    def get(self, request, pk, format=None):
        try:
            announcement = models.PrivateAnnouncement.objects.get(pk=pk)
        except models.PrivateAnnouncement.DoesNotExist:
            return Response({"error": "Объявление не существует"}, 400)
        user = announcement.user
        if not user:
            return Response({"error": "Пользователя не существует"}, 400)
        announcement_serializer = serializers.PrivateAnnouncementDetailSerializer(announcement)
        user_serializer = serializers.UserAnnouncementSerializer(user)        

        response = {
            'announcement_detail': announcement_serializer.data,
            'user': user_serializer.data,
        }
        return Response(response, 200)
    