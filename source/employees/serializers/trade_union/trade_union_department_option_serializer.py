from typing import List
from rest_framework import serializers

from ...models import TradeUnionDepartmentOptionModel


class TradeUnionDepartmentOptionSerializer(serializers.ModelSerializer):
    hierarchy = serializers.SerializerMethodField()

    def get_hierarchy(self, obj: TradeUnionDepartmentOptionModel):
        return [ancestor.label for ancestor in obj.get_ancestors().all()]  # type: ignore

    class Meta:
        model = TradeUnionDepartmentOptionModel
        fields = ["id", "path", "label", "hierarchy"]
