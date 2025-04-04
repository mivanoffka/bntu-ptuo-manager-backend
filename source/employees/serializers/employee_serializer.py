from os import read
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
        fields = ("id", "employee_versions", "employee_version")

    employee_versions = EmployeeVersionSerializer(many=True, read_only=True)
    employee_version = EmployeeVersionSerializer(write_only=True)

    def create(self, validated_data):
        instance = EmployeeModel.objects.create()

        employee_version_data = validated_data.pop("employee_version")
        employee_version_data["employee"] = instance

        EmployeeVersionSerializer().create(employee_version_data)

        return instance

    def update(self, instance: EmployeeModel, validated_data):
        employee_version_data = validated_data.pop("employee_version")
        employee_version_data["employee"] = instance

        EmployeeVersionSerializer().create(employee_version_data)

        return instance

    def delete(self, instance: EmployeeModel):
        instance.delete()
