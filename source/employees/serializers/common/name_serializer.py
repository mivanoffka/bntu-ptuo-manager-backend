from rest_framework import serializers

from ..abstract.deserializer import Deserializer
from ...models import NameModel


class NameSerializer(Deserializer):
    class Meta(Deserializer.Meta):
        model = NameModel
        fields = ["id", "first_name", "middle_name", "last_name", "created_at"]
