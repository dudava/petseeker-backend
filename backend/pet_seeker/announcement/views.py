from django.contrib.auth.models import User
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response

from . import models, serializers

class AnnouncementCreateEditViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Announcement.objects.all()
    serializer_class = serializers.AnnouncementSerializer

    def perform_create(self, serializer):
        serializer.save(user=User.objects.first())


class AnnouncementDeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
    def delete(self, request, pk, format=None):
        try:
            announcement = models.Announcement.objects.get(pk=pk)
        except models.Announcement.DoesNotExist:
            return Response({"error": "Объявление не существует"}, 400)
        announcement.delete()
        return Response({"success": "Объявление удалено"}, 200)


class AnnouncementDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = serializers.AnnouncementDetailSerializer

    def get(self, request, pk, format=None):
        try:
            announcement = models.Announcement.objects.get(pk=pk)
        except models.Announcement.DoesNotExist:
            return Response({"error": "Объявление не существует"}, 400)
        user = announcement.user
        if not user:
            return Response({"error": "Пользователя не существует"}, 400)
        announcement_serializer = serializers.AnnouncementSerializer(announcement)
        user_serializer = serializers.UserAnnouncementSerializer(user)        

        detail_serializer = serializers.AnnouncementDetailSerializer(data={
            'announcement_detail': announcement_serializer.data,
            'user': user_serializer.data,
        })
        detail_serializer.is_valid(raise_exception=True)
        response = detail_serializer.validated_data
        return Response(response, 200)