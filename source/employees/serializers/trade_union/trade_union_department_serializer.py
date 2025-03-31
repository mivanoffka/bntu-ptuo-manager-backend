from rest_framework import serializers

from .trade_union_department_option_serializer import (
    TradeUnionDepartmentOptionSerializer,
)

from ...models import TradeUnionDepartment


class TradeUnionDepartmentSerializer(serializers.ModelSerializer):
    trade_union_department_option = serializers.SerializerMethodField()

    def get_trade_union_department_option(self, obj: TradeUnionDepartment):
        return TradeUnionDepartmentOptionSerializer(
            obj.trade_union_department_option
        ).data

    class Meta:
        model = TradeUnionDepartment
        fields = ["id", "trade_union_department_option"]
