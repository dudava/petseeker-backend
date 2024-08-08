from rest_framework import serializers


class StatusEnumField(serializers.SerializerMethodField):
    def to_representation(self, value):
        obj = self.parent.instance
        return obj.get_status_display().lower().replace(' ', '_')


class StateEnumField(serializers.SerializerMethodField):
    def to_representation(self, value):
        obj = self.parent.instance
        return obj.get_state_display().lower().replace(' ', '_')


class PetTypeEnumField(serializers.SerializerMethodField):
    def to_representation(self, value):
        obj = self.parent.instance
        return obj.get_pet_type_display().lower().replace(' ', '_')



