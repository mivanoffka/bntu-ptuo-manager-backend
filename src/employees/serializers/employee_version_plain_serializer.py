from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    SerializerMethodField,
)

from trees.models import BntuDepartmentModel

from ..models import (
    EmployeeVersionModel,
)
from .other import CommentSerializer, RelativeSerializer, RewardSerializer
from .bntu import BntuPositionSerializer
from .contacts import EmailSerializer, AddressSerializer, PhoneNumberSerializer
from .trade_union import TradeUnionPositionSerializer
from .education import EducationalInstitutionSerializer


class EmployeeVersionPlainSerializer(ModelSerializer):
    # region Common

    first_name = CharField(required=False, allow_null=True, allow_blank=True)
    last_name = CharField(required=False, allow_null=True, allow_blank=True)
    middle_name = CharField(required=False, allow_null=True, allow_blank=True)

    gender = SerializerMethodField()

    # endregion

    # region Contacts

    emails = EmailSerializer(many=True)
    phone_numbers = PhoneNumberSerializer(many=True)
    addresses = AddressSerializer(many=True)

    # endregion

    # region Education

    educational_institutions = EducationalInstitutionSerializer(many=True)
    education_level = SerializerMethodField()
    academic_degree = SerializerMethodField()

    # endregion

    # region BNTU

    bntu_positions = SerializerMethodField()

    # endregion

    # region TradeUnion

    trade_union_positions = TradeUnionPositionSerializer(many=True)
    trade_union_department_path = CharField(
        required=False, allow_null=True, allow_blank=True
    )
    working_group = SerializerMethodField()

    # endregion

    # region Other

    comments = CommentSerializer(many=True)
    relatives = RelativeSerializer(many=True)
    rewards = RewardSerializer(many=True)

    # endregion

    def get_gender(self, obj):
        return getattr(obj.gender, "label", None)

    def get_education_level(self, obj):
        return getattr(obj.education_level, "label", None)

    def get_academic_degree(self, obj):
        return getattr(obj.academic_degree, "label", None)

    def get_working_group(self, obj):
        return getattr(obj.working_group, "label", None)

    def get_bntu_positions(self, obj):
        bntu_positions_raw = BntuPositionSerializer(obj.bntu_positions, many=True)
        bntu_positions = []

        for bntu_position_raw in bntu_positions_raw.data:
            department = BntuDepartmentModel.objects.get(
                path=bntu_position_raw["bntu_department_path"]
            )

            bntu_position = {
                "position": bntu_position_raw["label"],
                "department": department.label,
            }

            bntu_positions.append(bntu_position)

        return bntu_positions

    class Meta:
        model = EmployeeVersionModel
        fields = (
            "id",
            "last_name",
            "first_name",
            "middle_name",
            "birthdate",
            "birthplace",
            "gender",
            "bntu_positions",
            "trade_union_positions",
            "trade_union_department_path",
            "trade_union_department_authentic_label",
            "working_group",
            "working_group_authentic_label",
            "joined_at",
            "recorded_at",
            "is_archived",
            "is_retired",
            "archived_at",
            "retired_at",
            "educational_institutions",
            "education_level",
            "academic_degree",
            "phone_numbers",
            "addresses",
            "emails",
            "comments",
            "rewards",
            "relatives",
            "created_at",
        )
        read_only_fields = [
            "working_group_authentic_label",
            "trade_union_department_authentic_label",
            "created_at",
        ]
