from encodings.punycode import T
from rest_framework import serializers

from .abstract.deserializer import Deserializer

from ..models.trade_union.working_group_model import WorkingGroupModel

from .other import CommentSerializer, RelativeSerializer, RewardSerializer

from .education import (
    EducationLevelSerializer,
    AcademicDegreeSerializer,
    EducationalInstitutionSerializer,
)

from .common import GenderSerializer, NameSerializer

from .bntu import BntuPositionSerializer

from .contacts import EmailSerializer, AddressSerializer, PhoneNumberSerializer

from .trade_union import (
    WorkingGroupSerializer,
    TradeUnionPositionSerializer,
    TradeUnionDepartmentSerializer,
)

from .generic import History

from ..models import EmployeeModel, NameModel, TradeUnionDepartmentModel


class EmployeeSerializer(Deserializer):

    # region Common

    names = NameSerializer(many=True)
    gender = GenderSerializer()

    # endregion

    # region Contacts

    emails = EmailSerializer(many=True)
    phone_numbers = PhoneNumberSerializer(many=True)
    addresses = AddressSerializer(many=True)

    # endregion

    # region Education

    educational_institutions = EducationalInstitutionSerializer(many=True)
    education_level = EducationLevelSerializer()
    academic_degree = AcademicDegreeSerializer()

    # endregion

    # region BNTU

    bntu_positions = BntuPositionSerializer(many=True)

    # endregion

    # region TradeUnion

    trade_union_positions = TradeUnionPositionSerializer(many=True)
    trade_union_departments = TradeUnionDepartmentSerializer(many=True)
    working_groups = WorkingGroupSerializer(many=True)

    # endregion

    # region Other

    comments = CommentSerializer(many=True)
    relatives = RelativeSerializer(many=True)
    rewards = RewardSerializer(many=True)

    # endregion

    class Meta(Deserializer.Meta):
        model = EmployeeModel
        fields = [
            "id",
            "names",
            "birthdate",
            "birthplace",
            "gender",
            "bntu_positions",
            "trade_union_positions",
            "trade_union_departments",
            "working_groups",
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
        ]
