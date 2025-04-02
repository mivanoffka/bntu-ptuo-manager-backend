from rest_framework import serializers

from ..abstract.deserializer import Deserializer

from ...models import RelativeTypeModel


class RelativeTypeSerializer(Deserializer):
    class Meta(Deserializer.Meta):
        model = RelativeTypeModel
        fields = ["id", "label"]
