from rest_framework import serializers

from ..abstract.deserializer import Deserializer
from ...models import EmailModel


class EmailSerializer(Deserializer):
    class Meta(Deserializer.Meta):
        model = EmailModel
        fields = ["id", "value", "comment"]
