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
        return Response(services.get_user_info(request.user), 200)


class UserInfoEditView(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = UserInfoSerializer
    queryset = models.UserInfo.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user_info = models.UserInfo.objects.get(user=request.user)
        serializer = UserInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance=user_info, validated_data=serializer.validated_data)
        return Response(serializer.validated_data, 200)


class UserDeleteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def delete(self, request, pk, format=None):
        try:
            user = models.UserInfo.objects.get(pk=pk)
            user_custom = models.CustomUser.objects.get(pk=pk)
            permission = IsOwnerOrReadOnly()
            if not permission.has_object_permission(request, self, user):
                return Response({"error": "У вас нет прав для удаления этого пользователя или пользователь не "
                                          "существует"}, 403)
        except models.CustomUser.DoesNotExist:
            return Response({"error": "У вас нет прав для удаления этого пользователя или пользователя не существует"},
                            403)

        user_custom.delete()
        return Response({"success": "Пользователь успешно удален"}, 200)
