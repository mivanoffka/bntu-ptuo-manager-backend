from rest_framework import serializers

from ...models import TradeUnionPosition


class TradeUnionPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionPosition
        fields = ["id", "label", "occurred_at", "comment"]
