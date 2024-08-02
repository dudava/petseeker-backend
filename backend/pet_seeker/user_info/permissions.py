from rest_framework import permissions
from shelter.models import Shelter
from shelter_announcement.models import ShelterAnnouncement
from announcement.models import PrivateAnnouncement
from rating.models import UserFeedback

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user
    
class IsShelterOwnerByAnnouncementQueryParamsOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        request_url = request.build_absolute_uri()
        shelter_announcement_pk = int(request_url.split('/')[-2])
        
        try:
            announcement = ShelterAnnouncement.objects.get(pk=shelter_announcement_pk)
        except ShelterAnnouncement.DoesNotExist:
            return False
        return announcement.shelter.user == request.user


class IsShelterOwnerByQueryParamsOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        request_url = request.build_absolute_uri()
        shelter_pk = int(request_url.split('/')[-2])
        
        try:
            shelter = Shelter.objects.get(pk=shelter_pk)
        except Shelter.DoesNotExist:
            return False
        return shelter.user == request.user


class IsAnnouncementShelterOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        shelter_pk = request.data.get('shelter')
        
        try:
            shelter = Shelter.objects.get(pk=shelter_pk)
        except Shelter.DoesNotExist:
            return False
        return shelter.user == request.user


class IsPrivateAnnouncementOwnerByQueryParamsOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        request_url = request.build_absolute_uri()
        private_announcement_pk = int(request_url.split('/')[-2])
        
        try:
            private_announcement = PrivateAnnouncement.objects.get(pk=private_announcement_pk)
        except PrivateAnnouncement.DoesNotExist:
            return False
        return private_announcement.user == request.user
    
class IsFeedOwnerByQueryParamsOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        request_url = request.build_absolute_uri()
        feed_pk = int(request_url.split('/')[-2])
        
        try:
            feed = UserFeedback.objects.get(pk=feed_pk)
        except UserFeedback.DoesNotExist:
            return False
        return feed.user == request.user