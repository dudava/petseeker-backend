from announcement.models import Announcement


def get_last_10_announcements():
    return Announcement.objects.all()[:10]
