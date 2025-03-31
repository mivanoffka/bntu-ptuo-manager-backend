from rest_framework import serializers

from .trade_union_department_option_serializer import (
    TradeUnionDepartmentOptionSerializer,
)

from ...models import TradeUnionDepartmentModel


class TradeUnionDepartmentSerializer(serializers.ModelSerializer):
    trade_union_department_option = serializers.SerializerMethodField()

    def get_trade_union_department_option(self, obj: TradeUnionDepartmentModel):
        return TradeUnionDepartmentOptionSerializer(
            obj.trade_union_department_option
        ).data

    class Meta:
        model = TradeUnionDepartmentModel
        fields = ["id", "trade_union_department_option"]
