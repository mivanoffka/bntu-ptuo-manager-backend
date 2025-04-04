from rest_framework.serializers import ModelSerializer

from .employee_version_serializer import EmployeeVersionSerializer
from ..models import (
    EmployeeVersionModel,
    EmployeeModel,
    NameModel,
    EmailModel,
    PhoneNumberModel,
    AddressModel,
    EducationalInstitutionModel,
    BntuPositionModel,
    TradeUnionPositionModel,
    TradeUnionDepartmentRecordModel,
    WorkingGroupRecordModel,
    CommentModel,
    RelativeModel,
    RewardModel,
)


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = (
            "id",
            "employee_versions",
        )

    employee_versions = EmployeeVersionSerializer(many=True)

    def create(self, validated_data):
        instance = EmployeeModel.objects.create()

        employee_version_data = validated_data.pop("employee_versions")[0]

        model_map = {
            "names": NameModel,
            "emails": EmailModel,
            "phone_numbers": PhoneNumberModel,
            "addresses": AddressModel,
            "educational_institutions": EducationalInstitutionModel,
            "bntu_positions": BntuPositionModel,
            "trade_union_positions": TradeUnionPositionModel,
            "trade_union_department_records": TradeUnionDepartmentRecordModel,
            "working_group_records": WorkingGroupRecordModel,
            "comments": CommentModel,
            "relatives": RelativeModel,
            "rewards": RewardModel,
        }

        related_data = {
            field: employee_version_data.pop(field, []) for field in model_map.keys()
        }
        employee_version = EmployeeVersionModel.objects.create(
            employee=instance, **employee_version_data
        )

        for field, data_list in related_data.items():
            model_class = model_map[field]
            for data in data_list:
                if "id" in data.keys():
                    data.pop("id")
                model_class.objects.create(employee_version=employee_version, **data)

        return instance

    def update(self, instance: EmployeeModel, validated_data):
        employee_version_data = validated_data.pop("employee_versions")[0]

        model_map = {
            "names": NameModel,
            "emails": EmailModel,
            "phone_numbers": PhoneNumberModel,
            "addresses": AddressModel,
            "educational_institutions": EducationalInstitutionModel,
            "bntu_positions": BntuPositionModel,
            "trade_union_positions": TradeUnionPositionModel,
            "trade_union_department_records": TradeUnionDepartmentRecordModel,
            "working_group_records": WorkingGroupRecordModel,
            "comments": CommentModel,
            "relatives": RelativeModel,
            "rewards": RewardModel,
        }

        related_data = {
            field: employee_version_data.pop(field, []) for field in model_map.keys()
        }
        employee_version = EmployeeVersionModel.objects.create(
            employee=instance, **employee_version_data
        )

        for field, data_list in related_data.items():
            model_class = model_map[field]
            for data in data_list:
                if "id" in data.keys():
                    data.pop("id")
                model_class.objects.create(employee_version=employee_version, **data)

        return instance

    def delete(self, instance: EmployeeModel):
        instance.delete()
