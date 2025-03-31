from typing import List
from rest_framework import serializers

from ...models import TradeUnionDepartmentOption


class TradeUnionDepartmentOptionSerializer(serializers.ModelSerializer):
    hierarchy = serializers.SerializerMethodField()

    def get_hierarchy(self, obj: TradeUnionDepartmentOption):
        return [ancestor.label for ancestor in obj.get_ancestors().all()]  # type: ignore

    class Meta:
        model = TradeUnionDepartmentOption
        fields = ["id", "path", "label", "hierarchy"]
