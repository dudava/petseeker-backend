from rest_framework import viewsets, mixins, generics
from django.core.exceptions import FieldError
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from announcement.serializers import PrivateAnnouncementListSerializer
from . import services
from . import serializers


class BaseAnnouncementSearchViewSet(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = serializers.CommonAnnouncementListSerializer

    def get_announcements(self, filter_params, page, page_size):
        raise NotImplementedError("Этот метод должен быть реализован в дочернем классе")

    def get(self, request, *args, **kwargs):
        filter_params = {key: request.query_params[key] for key in request.query_params}
        page = int(filter_params.pop('page', 1))
        page_size = int(filter_params.pop('page_size', 10))

        try:
            announcements = self.get_announcements(filter_params, page, page_size)
        except FieldError:
            return Response({"error": "Неверные параметры"}, 400)

        serializer = self.serializer_class(announcements, many=True)

        count = len(announcements)
        prev_url = request.build_absolute_uri().replace(f'page={str(page)}', f'page={page - 1}')
        if page - 1 < 1:
            prev_url = None
        next_url = request.build_absolute_uri().replace(f'page={str(page)}', f'page={page + 1}')
        if count < page_size:
            next_url = None

        return Response({
            'count': count,
            'next': next_url,
            'previous': prev_url,
            'results': serializer.data
        }, 200)


class AnnouncementSearchViewSet(BaseAnnouncementSearchViewSet):
    def get_announcements(self, filter_params, page, page_size):
        return services.get_announcements(filter_params, page, page_size)


class PrivateAnnouncementSearchViewSet(BaseAnnouncementSearchViewSet):
    def get_announcements(self, filter_params, page, page_size):
        return services.get_private_announcements(filter_params, page, page_size)


class ShelterAnnouncementSearchViewSet(BaseAnnouncementSearchViewSet):
    def get_announcements(self, filter_params, page, page_size):
        return services.get_shelter_announcements(filter_params, page, page_size)
