from rest_framework import serializers
from .models import UserFeedback


class UserFeedbackSerializer(serializers.ModelSerializer):
    user_by = serializers.ReadOnlyField(source='user_by.id')
    user_to = serializers.ReadOnlyField(source='user_to.id')
    class Meta:
        model = UserFeedback
        fields = '__all__'