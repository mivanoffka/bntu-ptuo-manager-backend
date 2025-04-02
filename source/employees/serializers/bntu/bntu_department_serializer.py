from typing import List
from rest_framework import serializers

from ..abstract.deserializer import Deserializer

from ...models.bntu.bntu_department_model import BntuDepartmentModel
from ...models import NameModel


class BntuDepartmentSerializer(Deserializer):
    hierarchy = serializers.SerializerMethodField()

    def get_hierarchy(self, obj: BntuDepartmentModel):
        return [ancestor.label for ancestor in obj.get_ancestors().all()]  # type: ignore

    class Meta(Deserializer.Meta):
        model = BntuDepartmentModel
        fields = ["id", "path", "label", "hierarchy"]
