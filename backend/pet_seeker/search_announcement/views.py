from rest_framework import viewsets, mixins, generics
import django_filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from announcement.serializers import PrivateAnnouncementListSerializer
from . import services
from . import serializers


class AnnouncementPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AnnouncementFilter(django_filters.FilterSet):
    pet_type = django_filters.CharFilter(lookup_expr='exact')
    breed = django_filters.CharFilter(lookup_expr='exact')
    color = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        fields = ('pet_type', 'breed', 'color', )



class AnnouncementSearchViewSet(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = serializers.AnnouncementFilterSerializer 
    # работать будет (1)_(1), желательно page_size четный передавать
    def get(self, request, *args, **kwargs):
        filter_params = {_: request.query_params[_] for _ in request.query_params}
        page = int(filter_params.pop('page', 1))
        page_size = int(filter_params.pop('page_size', 10))
        announcements = services.get_announcements(filter_params, page, page_size)
        serializer = serializers.AnnouncementFilterSerializer(announcements, many=True)        

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
    