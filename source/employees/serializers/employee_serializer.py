from rest_framework import serializers

from ..models.trade_union.working_group import WorkingGroup

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

from ..utils.history import History

from ..models import Employee, Name, TradeUnionDepartment


class EmployeeSerializer(serializers.ModelSerializer):

    # region Common

    names = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()

    def get_names(self, obj: Employee):
        return History[Name].from_timestamped(obj.names).serialize(NameSerializer)

    def get_gender(self, obj: Employee):
        if not obj.gender:
            return None

        return GenderSerializer(obj.gender).data

    # endregion

    # region Contacts

    emails = serializers.SerializerMethodField()
    phone_numbers = serializers.SerializerMethodField()
    addresses = serializers.SerializerMethodField()

    def get_emails(self, obj: Employee):
        return (EmailSerializer(email).data for email in obj.emails.all())

    def get_phone_numbers(self, obj: Employee):
        return (
            PhoneNumberSerializer(phone_number).data
            for phone_number in obj.phone_numbers.all()
        )

    def get_addresses(self, obj: Employee):
        return (AddressSerializer(address).data for address in obj.addresses.all())

    # endregion

    # region Education

    educational_institutions = serializers.SerializerMethodField()
    education_level = serializers.SerializerMethodField()
    academic_degree = serializers.SerializerMethodField()

    def get_educational_institutions(self, obj: Employee):
        return (
            EducationalInstitutionSerializer(institution).data
            for institution in obj.educational_institutions.all()
        )

    def get_education_level(self, obj: Employee):
        if not obj.education_level:
            return None

        return EducationLevelSerializer(obj.education_level).data

    def get_academic_degree(self, obj: Employee):
        if not obj.academic_degree:
            return None

        return AcademicDegreeSerializer(obj.academic_degree).data

    # endregion

    # region BNTU

    bntu_positions = serializers.SerializerMethodField()

    def get_bntu_positions(self, obj: Employee):
        return (
            BntuPositionSerializer(position).data
            for position in obj.bntu_positions.all()
        )

    # endregion

    # region TradeUnion

    trade_union_positions = serializers.SerializerMethodField()
    trade_union_departments = serializers.SerializerMethodField()
    working_groups = serializers.SerializerMethodField()

    def get_trade_union_positions(self, obj: Employee):
        return (
            TradeUnionPositionSerializer(trade_union_position).data
            for trade_union_position in obj.trade_union_positions.all()
        )

    def get_trade_union_departments(self, obj: Employee):
        return (
            History[TradeUnionDepartment]
            .from_timestamped(obj.trade_union_departments)
            .serialize(TradeUnionDepartmentSerializer)
        )

    def get_working_groups(self, obj: Employee):
        return (
            History[WorkingGroup]
            .from_timestamped(obj.working_groups)
            .serialize(WorkingGroupSerializer)
        )

    # endregion

    # region Other

    comments = serializers.SerializerMethodField()
    relatives = serializers.SerializerMethodField()
    rewards = serializers.SerializerMethodField()

    def get_comments(self, obj: Employee):
        return (CommentSerializer(comment).data for comment in obj.comments.all())

    def get_relatives(self, obj: Employee):
        return (RelativeSerializer(relative).data for relative in obj.relatives.all())

    def get_rewards(self, obj: Employee):
        return (RewardSerializer(reward).data for reward in obj.rewards.all())

    # endregion

    class Meta:
        model = Employee
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
