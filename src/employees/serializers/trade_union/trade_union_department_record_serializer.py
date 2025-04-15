from rest_framework import serializers


from ...models import TradeUnionDepartmentRecordModel, TradeUnionDepartmentOptionModel


class TradeUnionDepartmentRecordSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    authentic_label = serializers.CharField(read_only=True)

    def create(self, validated_data):
        trade_union_department_option_path = validated_data[
            "trade_union_department_option_path"
        ]
        authentic_label = TradeUnionDepartmentOptionModel.objects.get(
            path=trade_union_department_option_path
        ).label

        instance = TradeUnionDepartmentRecordModel.objects.create(
            **validated_data, authentic_label=authentic_label
        )

        return instance

    class Meta:
        model = TradeUnionDepartmentRecordModel
        fields = [
            "id",
            "trade_union_department_option_path",
            "created_at",
            "authentic_label",
        ]
