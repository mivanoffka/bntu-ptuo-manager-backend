from rest_framework import serializers

from ..abstract.deserializer import Deserializer

from ...models import RewardModel


class RewardSerializer(Deserializer):
    class Meta(Deserializer.Meta):
        model = RewardModel
        fields = ["id", "label", "comment", "granted_at"]
