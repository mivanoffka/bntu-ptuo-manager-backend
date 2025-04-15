from rest_framework import serializers

from ...models import BntuPositionModel, BntuDepartmentOptionModel


class BntuPositionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data.pop("bntu_department_authentic_label")
        bntu_department_record_path = validated_data["bntu_department_record_path"]
        bntu_department_authentic_label = BntuDepartmentOptionModel.objects.get(
            path=bntu_department_record_path
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
            "bntu_department_option_path",
            "bntu_department_authentic_label",
            "is_discharged_voluntarily",
            "dischargement_comment",
        ]
