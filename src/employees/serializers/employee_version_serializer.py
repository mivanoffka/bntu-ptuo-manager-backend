from tkinter import W
from typing import TYPE_CHECKING
from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    CharField,
)

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
    EmployeeVersionModel,
    GenderModel,
    AcademicDegreeModel,
    TradeUnionDepartmentModel,
    WorkingGroupModel,
)


from .other import CommentSerializer, RelativeSerializer, RewardSerializer


from .bntu import BntuPositionSerializer

from .contacts import EmailSerializer, AddressSerializer, PhoneNumberSerializer

from .trade_union import (
    TradeUnionPositionSerializer,
)

from .education import EducationalInstitutionSerializer

if TYPE_CHECKING:
    from .employee_serializer import EmployeeSerializer


class EmployeeVersionSerializer(ModelSerializer):
    # region Common

    first_name = CharField(required=False, allow_null=True, allow_blank=True)
    last_name = CharField(required=False, allow_null=True, allow_blank=True)
    middle_name = CharField(required=False, allow_null=True, allow_blank=True)

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
    trade_union_department_path = CharField(
        required=False, allow_null=True, allow_blank=True
    )
    working_group_id = PrimaryKeyRelatedField(
        queryset=WorkingGroupModel.objects.all(),
        source="working_group",
        allow_null=True,
        required=False,
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
            "last_name",
            "first_name",
            "middle_name",
            "birthdate",
            "birthplace",
            "gender_id",
            "bntu_positions",
            "trade_union_positions",
            "trade_union_department_path",
            "trade_union_department_authentic_label",
            "working_group_id",
            "working_group_authentic_label",
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
        read_only_fields = [
            "working_group_authentic_label",
            "trade_union_department_authentic_label",
        ]

    emails = EmailSerializer(many=True)

    def create(self, validated_data):
        try:
            trade_union_department_path = validated_data.pop(
                "trade_union_department_path", None
            )
            if trade_union_department_path:
                trade_union_department_authentic_label = (
                    TradeUnionDepartmentModel.objects.get(
                        path=trade_union_department_path
                    ).label
                )
                validated_data["trade_union_department_authentic_label"] = (
                    trade_union_department_authentic_label
                )

            working_group = validated_data.pop("working_group")
            if working_group:
                working_group_authentic_label = working_group.label
                validated_data["working_group_authentic_label"] = (
                    working_group_authentic_label
                )

            model_map = {
                "emails": EmailModel,
                "phone_numbers": PhoneNumberModel,
                "addresses": AddressModel,
                "educational_institutions": EducationalInstitutionModel,
                "bntu_positions": BntuPositionModel,
                "trade_union_positions": TradeUnionPositionModel,
                "comments": CommentModel,
                "relatives": RelativeModel,
                "rewards": RewardModel,
            }
            related_data = {
                field: validated_data.pop(field, []) for field in model_map.keys()
            }
            employee_version = EmployeeVersionModel.objects.create(
                **validated_data,
            )

            for field, data_list in related_data.items():
                model_class = model_map[field]
                for data in data_list:
                    model_class.objects.create(
                        employee_version=employee_version, **data
                    )
        except Exception as error:
            print(error)
            raise error
