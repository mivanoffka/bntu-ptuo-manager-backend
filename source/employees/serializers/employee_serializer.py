from os import read
from re import S
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .common.name_serializer import NameSerializer

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
            "employee_version_timestamps",
            "latest_employee_version",
        )

    employee_version_timestamps = SerializerMethodField()
    latest_employee_version = SerializerMethodField()

    def get_employee_version_timestamps(self, instance: EmployeeModel):
        return (version.created_at for version in instance.employee_versions.all())

    def get_latest_employee_version(self, instance: EmployeeModel):
        return EmployeeVersionSerializer(
            instance.employee_versions.order_by("-created_at").first()
        ).data

    def create(self, validated_data):
        instance = EmployeeModel.objects.create()

        employee_version_data = validated_data.pop("latest_employee_version")
        employee_version_data["employee"] = instance

        EmployeeVersionSerializer().create(employee_version_data)

        return instance

    def update(self, instance: EmployeeModel, validated_data):
        employee_version_data = validated_data.pop("latest_employee_version")
        employee_version_data["employee"] = instance

        EmployeeVersionSerializer().create(employee_version_data)

        return instance

    def delete(self, instance: EmployeeModel):
        instance.delete()
