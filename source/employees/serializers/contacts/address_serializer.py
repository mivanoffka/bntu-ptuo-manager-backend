from rest_framework import serializers

from ..abstract.deserializer import Deserializer
from ...models import AddressModel


class AddressSerializer(Deserializer):
    class Meta(Deserializer.Meta):
        model = AddressModel
        fields = ["id", "value", "comment"]
