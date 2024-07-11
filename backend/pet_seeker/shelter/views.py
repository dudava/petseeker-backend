from django.contrib.auth.models import User
from rest_framework import views, generics, viewsets, mixins, exceptions
from rest_framework.response import Response
from .models import Shelter
from . import serializers


class ShelterCreateEditViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Shelter.objects.all()
    serializer_class = serializers.ShelterSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if not user.user_info.is_shelter_owner:
            raise exceptions.NotAcceptable("Вы не являетесь владельцем приюта(ов)")
        serializer.save(user=user)


class ShelterListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Shelter.objects.all()
    serializer_class = serializers.ShelterSerializer


class UserSheltersView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = serializers.ShelterSerializer

    def get(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "Пользователя не существует"}, 400)
        shelters = user.shelters.all()
        serializer = serializers.ShelterSerializer(shelters, many=True)
        response = serializer.data
        return Response(response, 200)


class ShelterDeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
    def delete(self, request, pk, format=None):
        try:
            shelter = Shelter.objects.get(pk=pk)
        except Shelter.DoesNotExist:
            return Response({"error": "Приют не существует"}, 400)
        shelter.delete()
        return Response({"success": "Приют удален"}, 200)


class ShelterDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = serializers.ShelterSerializer

    def get(self, request, pk, format=None):
        try:
            shelter = Shelter.objects.get(pk=pk)
        except Shelter.DoesNotExist:
            return Response({"error": "Приют не существует"}, 400)
        user = shelter.user
        if not user:
            return Response({"error": "Пользователя не существует"}, 400)
        shelter_serializer = serializers.ShelterSerializer(shelter)
        response = shelter_serializer.data
        
        return Response(response, 200)
    
