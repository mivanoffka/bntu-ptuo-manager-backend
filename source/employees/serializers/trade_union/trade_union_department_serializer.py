from rest_framework import serializers


from ...models import TradeUnionDepartmentModel, TradeUnionDepartmentOptionModel


class TradeUnionDepartmentSerializer(serializers.ModelSerializer):
    trade_union_department_option_id = serializers.PrimaryKeyRelatedField(
        queryset=TradeUnionDepartmentOptionModel.objects.all(),
        source="trade_union_department_option",
    )

    class Meta:
        model = TradeUnionDepartmentModel
        fields = ["id", "trade_union_department_option_id"]
