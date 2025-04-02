from rest_framework import serializers

from ..abstract.deserializer import Deserializer

from ...models import PhoneNumberModel

from .phone_number_type_serializer import PhoneNumberTypeSerializer


class PhoneNumberSerializer(Deserializer):
    phone_number_type = PhoneNumberTypeSerializer()

    class Meta(Deserializer.Meta):
        model = PhoneNumberModel
        fields = ["id", "value", "phone_number_type", "comment"]
