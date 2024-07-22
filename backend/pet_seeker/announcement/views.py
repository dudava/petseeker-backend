from django.contrib.auth.models import User
from rest_framework import generics, mixins, viewsets, permissions
from rest_framework.response import Response

from . import models, serializers
from user.permissions import IsOwnerOrReadOnly

class PrivateAnnouncementCreateEditViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = models.PrivateAnnouncement.objects.all()
    serializer_class = serializers.PrivateAnnouncementSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PrivateAnnouncementDeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    # TODO: защита от удаления не своих объявлений
    def delete(self, request, pk, format=None):
        try:
            announcement = models.PrivateAnnouncement.objects.get(pk=pk)
        except models.Announcement.DoesNotExist:
            return Response({"error": "Объявление не существует"}, 400)
        announcement.delete()
        return Response({"success": "Объявление удалено"}, 200)


class PrivateAnnouncementDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = serializers.PrivateAnnouncementDetailSerializer

    def get(self, request, pk, format=None):
        try:
            announcement = models.PrivateAnnouncement.objects.get(pk=pk)
        except models.PrivateAnnouncement.DoesNotExist:
            return Response({"error": "Объявление не существует"}, 400)
        user = announcement.user
        if not user:
            return Response({"error": "Пользователя не существует"}, 400)
        announcement_serializer = serializers.PrivateAnnouncementSerializer(announcement)
        user_serializer = serializers.UserAnnouncementSerializer(user)        

        detail_serializer = serializers.PrivateAnnouncementDetailSerializer(data={
            'announcement_detail': announcement_serializer.data,
            'user': user_serializer.data,
        })
        detail_serializer.is_valid(raise_exception=True)
        response = detail_serializer.validated_data
        return Response(response, 200)
    