from typing import List
from rest_framework import serializers

from ...models.bntu.bntu_department import BntuDepartment
from ...models import Name


class BntuDepartmentSerializer(serializers.ModelSerializer):
    hierarchy = serializers.SerializerMethodField()

    def get_hierarchy(self, obj: BntuDepartment):
        return [ancestor.label for ancestor in obj.get_ancestors().all()]  # type: ignore

    class Meta:
        model = BntuDepartment
        fields = ["id", "path", "label", "hierarchy"]
