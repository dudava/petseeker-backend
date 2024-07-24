from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import SmsVerificationCodeSerializer, SmsAuthSerializer
from . import services
from user.services import create_user_with_userinfo
from user.models import CustomUser

class SmsVerificationCodeCreateView(generics.CreateAPIView):
    serializer_class = SmsVerificationCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data.get('phone_number')
        services.create_verification_code(phone_number)
        return Response({"success": "СМС код отправлен"}, 200)
    

class SmsAuthView(generics.CreateAPIView):
    serializer_class = SmsAuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data.get('phone_number')
        code = serializer.validated_data.get('code')
        if not services.verificate_code(phone_number, code):
            return Response({"error": "Неверный код"}, 400)
        
        user = None
        if not CustomUser.objects.filter(phone_number=phone_number).exists():
            user, user_info = create_user_with_userinfo(serializer.validated_data)
        else:
            user = CustomUser.objects.get(phone_number=phone_number)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, 200)