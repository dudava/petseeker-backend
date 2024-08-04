import random

from announcement.models import PrivateAnnouncement
from shelter_announcement.models import ShelterAnnouncement


def get_announcements(filter_params, page, page_size=10):
    page_start = (page - 1) * page_size / 2
    page_end = page * page_size / 2
    private_announcements = PrivateAnnouncement.objects.filter(**filter_params)[page_start:page_end]
    shelter_announcements = ShelterAnnouncement.objects.filter(**filter_params)[page_start:page_end]
    announcements = [*private_announcements, *shelter_announcements]
    if private_announcements.count() < page_size / 2:
        additional_count = page_size / 2 - private_announcements.count()
        additional_shelter_announcements = ShelterAnnouncement.objects.filter(**filter_params)[page_end:page_end + additional_count]
        announcements += [*additional_shelter_announcements]
    elif shelter_announcements.count() < page_size / 2:
        additional_count = page_size / 2 - shelter_announcements.count()
        additional_private_announcements = PrivateAnnouncement.objects.filter(**filter_params)[page_end:page_end + additional_count]
        announcements += [*additional_private_announcements]
    return announcements

