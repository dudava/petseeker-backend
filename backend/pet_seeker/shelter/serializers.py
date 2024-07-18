from rest_framework import serializers
from .models import Shelter

class ShelterSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    lattitude_longitude = serializers.ReadOnlyField()
    
    class Meta:
        model = Shelter
        fields = '__all__'