from rest_framework import serializers

from ..abstract.deserializer import Deserializer

from .relative_type_serializer import RelativeTypeSerializer

from ...models import RelativeModel


class RelativeSerializer(Deserializer):
    relative_type = RelativeTypeSerializer()

    class Meta(Deserializer.Meta):
        model = RelativeModel
        fields = ["id", "full_name", "birthdate", "comment", "relative_type"]
