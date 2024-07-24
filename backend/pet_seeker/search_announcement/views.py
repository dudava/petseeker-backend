from rest_framework import viewsets, mixins
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from announcement.models import PrivateAnnouncement
from announcement.serializers import PrivateAnnouncementListSerializer
from rest_framework.pagination import PageNumberPagination


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