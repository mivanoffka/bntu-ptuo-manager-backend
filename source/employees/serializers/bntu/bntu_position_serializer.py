from rest_framework import serializers

from .bntu_department_serializer import BntuDepartmentSerializer

from ...models import BntuPosition


class BntuPositionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()

    def get_name(self, obj):
        if obj.name:
            return obj.name.label
        return None

    def get_department(self, obj):
        return BntuDepartmentSerializer(obj.department).data

    class Meta:
        model = BntuPosition
        fields = [
            "name",
            "hired_at",
            "is_discharged",
            "discharged_at",
            "department",
            "is_discharged_voluntarily",
            "dischargement_comment",
        ]
