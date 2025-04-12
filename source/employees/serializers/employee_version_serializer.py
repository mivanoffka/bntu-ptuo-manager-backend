from typing import TYPE_CHECKING
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from ..models import (
    RewardModel,
    RelativeModel,
    CommentModel,
    TradeUnionPositionModel,
    BntuPositionModel,
    EducationalInstitutionModel,
    AddressModel,
    PhoneNumberModel,
    EmailModel,
    EducationLevelModel,
    WorkingGroupRecordModel,
    EmployeeVersionModel,
    NameModel,
    TradeUnionDepartmentRecordModel,
    GenderModel,
    AcademicDegreeModel,
    EmployeeModel,
)


from .other import CommentSerializer, RelativeSerializer, RewardSerializer

from .common import NameSerializer

from .bntu import BntuPositionSerializer

from .contacts import EmailSerializer, AddressSerializer, PhoneNumberSerializer

from .trade_union import (
    WorkingGroupRecordSerializer,
    TradeUnionPositionSerializer,
    TradeUnionDepartmentRecordSerializer,
)

from .education import EducationalInstitutionSerializer

if TYPE_CHECKING:
    from .employee_serializer import EmployeeSerializer


class EmployeeVersionSerializer(ModelSerializer):
    # region Common

    names = NameSerializer(many=True)
    new_name = NameSerializer(write_only=True, required=False, allow_null=True)

    gender_id = PrimaryKeyRelatedField(
        queryset=GenderModel.objects.all(), source="gender"
    )

    # endregion

    # region Contacts

    emails = EmailSerializer(many=True)
    phone_numbers = PhoneNumberSerializer(many=True)
    addresses = AddressSerializer(many=True)

    # endregion

    # region Education

    educational_institutions = EducationalInstitutionSerializer(many=True)
    education_level_id = PrimaryKeyRelatedField(
        queryset=EducationLevelModel.objects.all(), source="education_level"
    )
    academic_degree_id = PrimaryKeyRelatedField(
        queryset=AcademicDegreeModel.objects.all(), source="academic_degree"
    )

    # endregion

    # region BNTU

    bntu_positions = BntuPositionSerializer(many=True)

    # endregion

    # region TradeUnion

    trade_union_positions = TradeUnionPositionSerializer(many=True)

    trade_union_department_records = TradeUnionDepartmentRecordSerializer(many=True)
    new_trade_union_department_record = TradeUnionDepartmentRecordSerializer(
        write_only=True, required=False, allow_null=True
    )

    working_group_records = WorkingGroupRecordSerializer(many=True)
    new_working_group_record = WorkingGroupRecordSerializer(
        write_only=True, required=False, allow_null=True
    )

    # endregion

    # region Other

    comments = CommentSerializer(many=True)
    relatives = RelativeSerializer(many=True)
    rewards = RewardSerializer(many=True)

    # endregion

    class Meta:
        model = EmployeeVersionModel
        fields = (
            "id",
            "names",
            "new_name",
            "birthdate",
            "birthplace",
            "gender_id",
            "bntu_positions",
            "trade_union_positions",
            "trade_union_department_records",
            "new_trade_union_department_record",
            "working_group_records",
            "new_working_group_record",
            "joined_at",
            "recorded_at",
            "is_archived",
            "is_retired",
            "archived_at",
            "retired_at",
            "educational_institutions",
            "education_level_id",
            "academic_degree_id",
            "phone_numbers",
            "addresses",
            "emails",
            "comments",
            "rewards",
            "relatives",
        )

    emails = EmailSerializer(many=True)

    def create(self, validated_data):
        try:
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

            new_items_fields = {
                "names": "new_name",
                "trade_union_department_records": "new_trade_union_department_record",
                "working_group_records": "new_working_group_record",
            }

            for items_field, new_item_field in new_items_fields.items():
                new_item = validated_data.pop(new_item_field, None)
                if new_item:
                    validated_data[items_field].append(new_item)

            related_data = {
                field: validated_data.pop(field, []) for field in model_map.keys()
            }
            employee_version = EmployeeVersionModel.objects.create(**validated_data)

            for field, data_list in related_data.items():
                model_class = model_map[field]
                for data in data_list:
                    model_class.objects.create(
                        employee_version=employee_version, **data
                    )
        except Exception as error:
            print(error)
            raise error
