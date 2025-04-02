from rest_framework import serializers

from ..abstract.deserializer import Deserializer

from ...models import GenderModel


class GenderSerializer(Deserializer):
    class Meta(Deserializer.Meta):
        model = GenderModel
        fields = ["id", "label"]
