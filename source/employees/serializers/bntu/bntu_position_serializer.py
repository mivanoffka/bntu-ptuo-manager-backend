from rest_framework import serializers

from ...models import BntuPositionModel, BntuDepartmentOptionModel


class BntuPositionSerializer(serializers.ModelSerializer):
    bntu_department_option_id = serializers.PrimaryKeyRelatedField(
        queryset=BntuDepartmentOptionModel.objects.all(),
        source="bntu_department_option",
    )

    def create(self, validated_data):
        validated_data.pop("bntu_department_authentic_label")
        bntu_department_record_id = validated_data["bntu_department_record_id"]
        bntu_department_authentic_label = BntuDepartmentOptionModel.objects.get(
            id=bntu_department_record_id
        ).label

        instance = BntuPositionModel(
            **validated_data,
            bntu_department_authentic_label=bntu_department_authentic_label
        )

        return instance

    class Meta:
        model = BntuPositionModel
        fields = [
            "id",
            "label",
            "hired_at",
            "is_discharged",
            "discharged_at",
            "bntu_department_option_id",
            "bntu_department_authentic_label",
            "is_discharged_voluntarily",
            "dischargement_comment",
        ]
