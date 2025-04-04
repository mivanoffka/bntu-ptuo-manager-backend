from urllib import request
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


class EmployeeVersionSerializer(ModelSerializer):
    # region Common

    names = NameSerializer(many=True)
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
    working_group_records = WorkingGroupRecordSerializer(many=True)

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
            "birthdate",
            "birthplace",
            "gender_id",
            "bntu_positions",
            "trade_union_positions",
            "trade_union_department_records",
            "working_group_records",
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
        print(validated_data)

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
            field: validated_data.pop(field, []) for field in model_map.keys()
        }
        employee = EmployeeVersionModel.objects.create(**validated_data)

        for field, data_list in related_data.items():
            model_class = model_map[field]
            for data in data_list:
                model_class.objects.create(employee=employee, **data)

        return employee
