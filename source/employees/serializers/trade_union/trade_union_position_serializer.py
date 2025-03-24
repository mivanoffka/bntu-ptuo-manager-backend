from rest_framework import serializers

from .working_group_serializer import WorkingGroupSerializer

from .trade_union_department_serializer import TradeUnionDepartmentSerializer


from ...models import TradeUnionPosition


class TradeUnionPositionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    working_group = serializers.SerializerMethodField()

    def get_name(self, obj):
        if obj.name:
            return obj.name.label
        return None

    def get_department(self, obj):
        return TradeUnionDepartmentSerializer(obj.department).data

    def get_working_group(self, obj):
        return WorkingGroupSerializer(obj.working_group).data

    class Meta:
        model = TradeUnionPosition
        fields = ["name", "joined_at", "left_at", "department", "working_group"]
