from rest_framework import viewsets, mixins, generics
import django_filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from announcement.models import PrivateAnnouncement
from shelter_announcement.models import ShelterAnnouncement
from announcement.serializers import PrivateAnnouncementListSerializer


class AnnouncementPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AnnouncementFilter(django_filters.FilterSet):
    pet_type = django_filters.CharFilter(lookup_expr='exact')
    breed = django_filters.CharFilter(lookup_expr='exact')
    color = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = PrivateAnnouncement
        fields = ('pet_type', 'breed', 'color', )



class AnnouncementSearchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PrivateAnnouncement.objects.all()
    serializer_class = PrivateAnnouncementListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnnouncementFilter
    pagination_class = AnnouncementPaginator

    def get_queryset(self, *args, **kwargs):
        filter_params = self.request.query_params
        private_announcements = PrivateAnnouncement.objects.filter(**filter_params)
        shelter_announcements = ShelterAnnouncement.objects.filter(**filter_params)
        return private_announcements