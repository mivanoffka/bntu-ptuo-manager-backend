from encodings.punycode import T
from rest_framework import serializers
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


class EmployeeSerializer(serializers.ModelSerializer):
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

    class Meta:
        plain_fields = (
            "id",
            "joined_at",
            "recorded_at",
            "is_archived",
            "is_retired",
            "archived_at",
            "retired_at",
            "birthdate",
            "birthplace",
        )
        list_fields = (
            "phone_numbers",
            "emails",
            "addresses",
            "comments",
            "rewards",
            "bntu_positions",
            "trade_union_positions",
            "relatives",
            "educational_institutions",
        )
        history_fields = ("names", "trade_union_departments", "working_groups")
        enum_fields = ("gender", "education_level", "academic_degree")
        model = EmployeeModel
        fields = (
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
        )

    emails = EmailSerializer(many=True)

    def _update_list(self, instance, field, validated_data):
        data = validated_data.pop(field, [])

        current_items = {
            item.id: item for item in instance.__getattribute__(field).all()
        }
        received_items_ids = {e["id"] for e in data if e.get("id")}

        for id in set(current_items.keys()) - received_items_ids:
            current_items[id].delete()

        for item_data in data:
            id = item_data.pop("id", None)

            if id and id in current_items:
                item = current_items[id]
                for attr, value in item_data.items():
                    setattr(item, attr, value)
                item.save()
            else:
                if id >= 0:
                    raise Exception("Unknown object")
                instance.__getattribute__(field).create(**item_data)

    def update(self, instance, validated_data):
        for field in self.Meta.list_fields:
            self._update_list(instance, field, validated_data)

        return super().update(instance, validated_data)
