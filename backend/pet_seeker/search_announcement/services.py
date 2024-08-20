from announcement.models import PrivateAnnouncement
from shelter_announcement.models import ShelterAnnouncement
from announcement.model_mixins import AnnouncementMixin
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def convert_age_filter_to_range(filter_params):
    age_filter = filter_params.get('age')

    if not age_filter:
        return filter_params

    start_age = None
    end_age = None

    if AnnouncementMixin.AgeCategoryChoices.SMALL in age_filter:
        start_age = 0
        end_age = 1

    if AnnouncementMixin.AgeCategoryChoices.YOUNG in age_filter:
        if start_age is None or 2 < start_age:
            start_age = 2
        if end_age is None or 7 > end_age:
            end_age = 7

    if AnnouncementMixin.AgeCategoryChoices.ADULT in age_filter:
        if start_age is None or 8 < start_age:
            start_age = 8
        if end_age is None or 12 > end_age:
            end_age = 12

    if AnnouncementMixin.AgeCategoryChoices.OLD in age_filter:
        if start_age is None or 13 < start_age:
            start_age = 13
        if end_age is None or 50 > end_age:
            end_age = 50

    if AnnouncementMixin.AgeCategoryChoices.UNKNOWN in age_filter:
        start_age = 0
        end_age = 50

    del filter_params['age']

    filter_params['age__range'] = (start_age, end_age)

    return filter_params


def full_text_search(filter_params):
    search_query = filter_params.pop('full_text_search', None)

    if search_query:
        search_query = SearchQuery(search_query)
        search_vector = SearchVector(
            'name', 'description', 'address',
            'pet_type', 'state', 'status',
            'breed', 'color', 'health_issues',
            'temperament')

        return {
            'search_query': search_query,
            'search_vector': search_vector
        }
    else:
        return {}


def get_announcements(filter_params, page, page_size=10):
    page_start = (page - 1) * page_size / 2
    page_end = page * page_size / 2

    filter_params = convert_age_filter_to_range(filter_params)
    search_params = full_text_search(filter_params)
    search_vector = search_params.get('search_vector')
    search_query = search_params.get('search_query')

    if search_query and search_vector:
        private_announcements = PrivateAnnouncement.objects.annotate(
            search_rank=SearchRank(search_vector, search_query)
        ).filter(
            search_rank__gt=0,
            **filter_params
        ).order_by('-search_rank')[page_start:page_end]

        shelter_announcements = ShelterAnnouncement.objects.annotate(
            search_rank=SearchRank(search_vector, search_query)
        ).filter(
            search_rank__gt=0,
            **filter_params
        ).order_by('-search_rank')[page_start:page_end]
    else:
        private_announcements = PrivateAnnouncement.objects.filter(**filter_params)[page_start:page_end]
        shelter_announcements = ShelterAnnouncement.objects.filter(**filter_params)[page_start:page_end]

    announcements = [*private_announcements, *shelter_announcements]

    if private_announcements.count() < page_size / 2:
        additional_count = page_size / 2 - private_announcements.count()

        if search_query and search_vector:
            additional_shelter_announcements = ShelterAnnouncement.objects.annotate(
                search_rank=SearchRank(search_vector, search_query)
            ).filter(
                search_rank__gt=0,
                **filter_params
            ).order_by('-search_rank')[page_start:page_end + additional_count]
        else:
            additional_shelter_announcements = ShelterAnnouncement.objects.filter(**filter_params)[page_end:page_end + additional_count]

        announcements += [*additional_shelter_announcements]
    elif shelter_announcements.count() < page_size / 2:
        additional_count = page_size / 2 - shelter_announcements.count()

        if search_query and search_vector:
            additional_private_announcements = PrivateAnnouncement.objects.annotate(
                search_rank=SearchRank(search_vector, search_query)
            ).filter(
                search_rank__gt=0,
                **filter_params
            ).order_by('-search_rank')[page_end:page_end + additional_count]
        else:
            additional_private_announcements = PrivateAnnouncement.objects.filter(**filter_params)[page_end:page_end + additional_count]

        announcements += [*additional_private_announcements]
    return announcements
