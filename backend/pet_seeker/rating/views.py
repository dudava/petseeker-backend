from django.core.exceptions import ValidationError
from rest_framework import viewsets, mixins, generics, views, exceptions, permissions
from rest_framework.response import Response
from .models import UserFeedback
from . import serializers
from user.permissions import IsOwnerOrReadOnly
from user.models import CustomUser


class UserFeedbackCreateEditViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = UserFeedback.objects.all()
    serializer_class = serializers.UserFeedbackSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        text = serializer.validated_data.get('text')
        mark = serializer.validated_data.get('mark')
        announcement = serializer.validated_data.get('announcement')
        try:
            serializer.save(
                user_by=self.request.user,
                user_to=announcement.user, 
                text=text, 
                mark=mark,
                announcement=announcement,
            )
        except ValidationError as ex:
            raise exceptions.ValidationError({"error": ex.message})


class UserFeedbackDeleteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def delete(self, request, pk, format=None):
        try:
            feedback = UserFeedback.objects.get(pk=pk)
        except UserFeedback.DoesNotExist:
            return Response({"error": "Отзыва не существует"}, 400)
        feedback.delete()
        return Response({"success": "Отзыв удален"}, 200)


class UserFeedbackListView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = serializers.UserFeedbackSerializer

    def get(self, request, pk, format=None):
        try:
            user = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"error": "Пользователя не существует"}, 400)
        feedbacks = user.feedbacks.all()
        serializer = self.serializer_class(feedbacks, many=True)
        response = serializer.data
        return Response(response, 200)