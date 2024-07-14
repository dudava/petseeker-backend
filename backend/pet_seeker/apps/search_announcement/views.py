from rest_framework import viewsets, mixins
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from announcement.models import Announcement
from announcement.serializers import AnnouncementSerializer
from rest_framework.pagination import PageNumberPagination


class AnnouncementPaginator(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


class AnnouncementFilter(django_filters.FilterSet):
    pet_type = django_filters.CharFilter(lookup_expr='exact')
    price = django_filters.RangeFilter()

    class Meta:
        model = Announcement
        fields = ('pet_type', 'price')



class AnnouncementSearchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnnouncementFilter
    pagination_class = AnnouncementPaginator