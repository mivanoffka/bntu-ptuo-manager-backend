from rest_framework import serializers

from ..abstract.deserializer import Deserializer

from ...models import PhoneNumberTypeModel


class PhoneNumberTypeSerializer(Deserializer):

    class Meta(Deserializer.Meta):
        model = PhoneNumberTypeModel
        fields = ["id", "label"]
