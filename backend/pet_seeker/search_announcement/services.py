from announcement.models import PrivateAnnouncement


def get_last_10_announcements():
    return PrivateAnnouncement.objects.all()[:10]
