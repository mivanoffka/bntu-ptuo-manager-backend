from rest_framework import serializers

from .enumerated_serializer import EnumeratedSerializer

from .bntu.bntu_position_serializer import BntuPositionSerializer

from .contacts import EmailSerializer, AddressSerializer, PhoneNumberSerializer
from .common import NameSerializer
from .education import EducationalInstitutionSerializer

from ..utils.history import History
from ..models import Employee, Name


class EmployeeSerializer(serializers.ModelSerializer):

    # region Common

    names = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()

    def get_names(self, obj: Employee):
        return History[Name].from_timestamped(obj.names).serialize(NameSerializer)

    def get_gender(self, obj: Employee):
        return EnumeratedSerializer.from_field(obj, "gender")

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

    def get_educational_institutions(self, obj: Employee):
        return (
            EducationalInstitutionSerializer(institution).data
            for institution in obj.educational_institutions.all()
        )

    def get_education_level(self, obj: Employee):
        return EnumeratedSerializer.from_field(obj, "education_level")

    def get_academic_degree(self, obj: Employee):
        return EnumeratedSerializer.from_field(obj, "academic_degree")

    # endregion

    # region BNTU

    bntu_positions = serializers.SerializerMethodField()

    def get_bntu_positions(self, obj: Employee):
        return (
            BntuPositionSerializer(position).data
            for position in obj.bntu_positions.all()
        )

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
            "joined_at",
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
