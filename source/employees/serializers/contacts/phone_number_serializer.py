from rest_framework import serializers

from ...models import PhoneNumber

from .phone_number_type_serializer import PhoneNumberTypeSerializer


class PhoneNumberSerializer(serializers.ModelSerializer):
    phone_number_type = serializers.SerializerMethodField()

    def get_phone_number_type(self, obj):
        return PhoneNumberTypeSerializer(obj.phone_number_type).data

    class Meta:
        model = PhoneNumber
        fields = ["id", "value", "phone_number_type", "comment"]
