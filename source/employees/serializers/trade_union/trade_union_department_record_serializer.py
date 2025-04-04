from rest_framework import serializers


from ...models import TradeUnionDepartmentRecordModel, TradeUnionDepartmentOptionModel


class TradeUnionDepartmentRecordSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    trade_union_department_option_id = serializers.PrimaryKeyRelatedField(
        queryset=TradeUnionDepartmentOptionModel.objects.all(),
        source="trade_union_department_option",
    )

    def create(self, validated_data):
        validated_data.pop("authentic_label")

        trade_union_department_option_id = validated_data[
            "trade_union_department_option_id"
        ]
        authentic_label = TradeUnionDepartmentOptionModel.objects.get(
            id=trade_union_department_option_id
        ).label

        instance = TradeUnionDepartmentOptionModel.objects.create(
            **validated_data, authentic_label=authentic_label
        )

        return instance

    class Meta:
        model = TradeUnionDepartmentRecordModel
        fields = [
            "id",
            "trade_union_department_option_id",
            "created_at",
            "authentic_label",
        ]
