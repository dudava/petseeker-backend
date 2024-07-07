from django.contrib.auth.models import User
from rest_framework import serializers, status, mixins, viewsets, permissions, generics, views
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly
import django.db

from . import models
from . import services
from .serializers import UserSerializer, UserInfoSerializer




class UserRegisterAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user, user_info = services.create_user_with_userinfo(serializer.validated_data)
        except django.db.IntegrityError:
            return Response({
                "error": "Пользователь с таким именем уже существует"
            }, status=400)
        return Response(services.get_user_info(user), status=201)


class UserDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = UserSerializer

    def get(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "Пользователя не существует"}, 400)
        response = services.get_user_info(user)
        return Response(response, 200)
    
class UserMeView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return services.get_user_info(request.user)


class UserInfoViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    queryset = models.UserInfo.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]