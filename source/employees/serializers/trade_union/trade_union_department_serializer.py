from typing import List
from rest_framework import serializers

from ...models import TradeUnionDepartment


class TradeUnionDepartmentSerializer(serializers.ModelSerializer):
    hierarchy = serializers.SerializerMethodField()

    def get_hierarchy(self, obj: TradeUnionDepartment):
        return [ancestor.label for ancestor in obj.get_ancestors().all()]  # type: ignore

    class Meta:
        model = TradeUnionDepartment
        fields = ["id", "path", "label", "hierarchy"]
