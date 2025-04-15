from rest_framework import serializers

from ...models import BntuPositionModel, BntuDepartmentModel


class BntuPositionSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        bntu_department_path = validated_data["bntu_department_path"]
        bntu_department_authentic_label = BntuDepartmentModel.objects.get(
            path=bntu_department_path
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
            "bntu_department_path",
            "bntu_department_authentic_label",
            "is_discharged_voluntarily",
            "dischargement_comment",
        ]
        read_only_fields = ["bntu_department_authentic_label"]
