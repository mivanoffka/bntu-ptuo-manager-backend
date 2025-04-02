from rest_framework import serializers

from ..abstract.deserializer import Deserializer

from ...models import CommentModel


class CommentSerializer(Deserializer):
    class Meta(Deserializer.Meta):
        model = CommentModel
        fields = ["id", "value"]
