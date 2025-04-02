from rest_framework import serializers

from ..abstract.deserializer import Deserializer

from .bntu_department_serializer import BntuDepartmentSerializer

from ...models import BntuPositionModel


class BntuPositionSerializer(Deserializer):
    department = BntuDepartmentSerializer()

    class Meta(Deserializer.Meta):
        model = BntuPositionModel
        fields = [
            "id",
            "label",
            "hired_at",
            "is_discharged",
            "discharged_at",
            "department",
            "is_discharged_voluntarily",
            "dischargement_comment",
        ]
