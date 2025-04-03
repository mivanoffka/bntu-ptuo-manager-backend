from rest_framework import serializers

from ...models import BntuPositionModel, BntuDepartmentModel


class BntuPositionSerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=BntuDepartmentModel.objects.all(),
    )

    class Meta:
        model = BntuPositionModel
        fields = [
            "id",
            "label",
            "hired_at",
            "is_discharged",
            "discharged_at",
            "department_id",
            "is_discharged_voluntarily",
            "dischargement_comment",
        ]
