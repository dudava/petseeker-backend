from rest_framework import serializers, status, mixins, viewsets, permissions, generics, views
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly

from . import models
from . import services
from .serializers import UserSerializer, UserInfoSerializer


class UserDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = UserSerializer

    def get(self, request, pk, format=None):
        print(request.user)
        try:
            user = models.CustomUser.objects.get(pk=pk)
        except models.CustomUser.DoesNotExist:
            return Response({"error": "Пользователя не существует"}, 400)
        response = services.get_user_info(user)
        return Response(response, 200)
    
class UserMeView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        return services.get_user_info(request.user)


class UserInfoEditView(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = UserInfoSerializer
    queryset = models.UserInfo.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def put(self, request):
        user_info = models.UserInfo.objects.get(user=request.user)
        serializer = UserInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance=user_info, validated_data=serializer.validated_data)
        return Response(serializer.validated_data, 200)
    