from rest_framework import viewsets, mixins, generics, views
from rest_framework.response import Response
from rest_framework import status
from .models import UserFeedback
from . import serializers 


class UserFeedbackCreateEditViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = UserFeedback.objects.all()
    serializer_class = serializers.UserFeedbackSerializer

    def perform_create(self, serializer):
        # serializer.save(user_by=self.request.user, user_to=)
        print(serializer.instance)