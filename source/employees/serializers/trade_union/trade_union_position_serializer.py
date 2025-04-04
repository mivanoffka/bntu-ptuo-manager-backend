from rest_framework import serializers

from ...models import TradeUnionPositionModel


class TradeUnionPositionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TradeUnionPositionModel
        fields = ["id", "label", "occurred_at", "comment"]
