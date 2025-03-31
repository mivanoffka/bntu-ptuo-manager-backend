from rest_framework import serializers

from .bntu_department_serializer import BntuDepartmentSerializer

from ...models import BntuPositionModel


class BntuPositionSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()

    def get_department(self, obj):
        return BntuDepartmentSerializer(obj.department).data

    class Meta:
        model = BntuPositionModel
        fields = [
            "label",
            "hired_at",
            "is_discharged",
            "discharged_at",
            "department",
            "is_discharged_voluntarily",
            "dischargement_comment",
        ]
