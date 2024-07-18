from rest_framework import viewsets, mixins, generics, views
from rest_framework.response import Response
from rest_framework import status
from .models import UserFeedback
from . import serializers 


class UserFeedbackCreateEditViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = UserFeedback.objects.all()
    serializer_class = serializers.UserFeedbackSerializer

    def perform_create(self, serializer):
        text = serializer.validated_data.get('text')
        mark = serializer.validated_data.get('mark')
        announcement = serializer.validated_data.get('announcement')
        serializer.save(
            user_by=self.request.user,
            user_to=announcement.user, 
            text=text, 
            mark=mark,
            announcement=announcement,
        )
        

class UserFeedbackDeleteView(views.APIView):
    def delete(self, request, pk, format=None):
        try:
            feedback = UserFeedback.objects.get(pk=pk)
        except UserFeedback.DoesNotExist:
            return Response({"error": "Отзыва не существует"}, 400)
        feedback.delete()
        return Response({"success": "Отзыв удален"}, 200)


