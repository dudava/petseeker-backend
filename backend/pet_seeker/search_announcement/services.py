from announcement.models import PrivateAnnouncement
from shelter_announcement.models import ShelterAnnouncement
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def paginate(queryset, page_start, page_end):
    return queryset[page_start:page_end]


def prepare_params(filter_params, page, page_size):
    page_start = (page - 1) * page_size // 2
    page_end = page * page_size // 2

    search_params = full_text_search(filter_params)
    search_vector = search_params.get('search_vector')
    search_query = search_params.get('search_query')

    return page_start, page_end, search_vector, search_query


def get_announcements_by_type(model, filter_params, search_vector, search_query, page_start, page_end):
    if search_query and search_vector:
        announcements = model.objects.annotate(
            search_rank=SearchRank(search_vector, search_query)
        ).filter(
            search_rank__gt=0,
            **filter_params
        ).order_by('-search_rank')[page_start:page_end]
    else:
        announcements = model.objects.filter(**filter_params)[page_start:page_end]

    return announcements


def full_text_search(filter_params):
    search_query = filter_params.pop('full_text_search', None)

    if search_query:
        search_query = SearchQuery(search_query)
        search_vector = SearchVector(
            'name', 'description', 'address',
            'pet_type', 'state', 'status',
            'breed', 'health_issues',
            'temperament')

        return {
            'search_query': search_query,
            'search_vector': search_vector
        }
    else:
        return {}


def get_announcements(filter_params, page, page_size=10):
    page_start, page_end, search_vector, search_query = prepare_params(filter_params, page, page_size)

    private_announcements = get_announcements_by_type(
        PrivateAnnouncement, filter_params, search_vector, search_query, page_start, page_end
    )

    shelter_announcements = get_announcements_by_type(
        ShelterAnnouncement, filter_params, search_vector, search_query, page_start, page_end
    )

    announcements = [*private_announcements, *shelter_announcements]

    if len(private_announcements) < page_size // 2:
        additional_count = page_size // 2 - len(private_announcements)
        additional_shelter_announcements = get_announcements_by_type(
            ShelterAnnouncement, filter_params, search_vector, search_query, page_end, page_end + additional_count
        )
        announcements += [*additional_shelter_announcements]

    elif len(shelter_announcements) < page_size // 2:
        additional_count = page_size // 2 - len(shelter_announcements)
        additional_private_announcements = get_announcements_by_type(
            PrivateAnnouncement, filter_params, search_vector, search_query, page_end, page_end + additional_count
        )
        announcements += [*additional_private_announcements]

    return announcements


def get_private_announcements(filter_params, page, page_size=10):
    page_size *= 2
    page_start, page_end, search_vector, search_query = prepare_params(filter_params, page, page_size)

    private_announcements = get_announcements_by_type(
        PrivateAnnouncement, filter_params, search_vector, search_query, page_start, page_end
    )

    return private_announcements


def get_shelter_announcements(filter_params, page, page_size=20):
    page_size *= 2
    page_start, page_end, search_vector, search_query = prepare_params(filter_params, page, page_size)

    shelter_announcements = get_announcements_by_type(
        ShelterAnnouncement, filter_params, search_vector, search_query, page_start, page_end
    )

    return shelter_announcements
