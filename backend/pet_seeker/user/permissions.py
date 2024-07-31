from rest_framework import permissions
from shelter.models import Shelter
from shelter_announcement.models import ShelterAnnouncement


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
    
class IsShelterOwnerByQueryParamsOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        request_url = request.build_absolute_uri()
        print(request_url)
        print(request_url.split('/'))
        shelter_announcement_pk = int(request_url.split('/')[-2])
        
        try:
            announcement = ShelterAnnouncement.objects.get(pk=shelter_announcement_pk)
        except ShelterAnnouncement.DoesNotExist:
            return False
        return announcement.shelter.user == request.user