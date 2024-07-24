from rest_framework import serializers


class SmsVerificationCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField()


class SmsAuthSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.CharField()