from rest_framework import serializers


from ...models import PhoneNumberModel

from .phone_number_type_serializer import PhoneNumberTypeSerializer


class PhoneNumberSerializer(serializers.ModelSerializer):
    phone_number_type = PhoneNumberTypeSerializer()

    class Meta:
        model = PhoneNumberModel
        fields = ["id", "value", "phone_number_type", "comment"]
