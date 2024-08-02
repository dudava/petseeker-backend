from rest_framework import authentication, exceptions
from rest_framework.authtoken.models import Token


class HTTPOnlyCookieAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('token')
        if not token:
            return None
        try:
            user = Token.objects.get(key=token).user
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')
        return (user, None)

    def authenticate_header(self, request):
        return 'Cookie'