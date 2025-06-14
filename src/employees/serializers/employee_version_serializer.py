from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    CharField,
)

from media.serializers import ImageSerializer
from references.models import (
    GenderModel,
    WorkingGroupModel,
    AcademicDegreeModel,
    EducationLevelModel,
    ExemptionModel,
)
from media.models import ImageModel
from ..models import (
    RewardModel,
    RelativeModel,
    CommentModel,
    BntuPositionModel,
    EducationalInstitutionModel,
    AddressModel,
    PhoneNumberModel,
    EmailModel,
    EmployeeVersionModel,
)
from .other import CommentSerializer, RelativeSerializer, RewardSerializer
from .bntu import BntuPositionSerializer
from .contacts import EmailSerializer, AddressSerializer, PhoneNumberSerializer
from .education import EducationalInstitutionSerializer
from trees.models import TradeUnionDepartmentModel


class EmployeeVersionSerializer(ModelSerializer):
    # region Common

    first_name = CharField()
    last_name = CharField()
    middle_name = CharField(allow_null=True, allow_blank=True)

    gender_id = PrimaryKeyRelatedField(
        queryset=GenderModel.objects.all(), source="gender"
    )

    image_path = CharField(allow_null=True)

    # endregion

    # region Contacts

    emails = EmailSerializer(many=True)
    phone_numbers = PhoneNumberSerializer(many=True)
    addresses = AddressSerializer(many=True)

    # endregion

    # region Education

    educational_institutions = EducationalInstitutionSerializer(many=True)
    education_level_id = PrimaryKeyRelatedField(
        queryset=EducationLevelModel.objects.all(),
        source="education_level",
        allow_null=True,
    )
    academic_degree_id = PrimaryKeyRelatedField(
        queryset=AcademicDegreeModel.objects.all(),
        source="academic_degree",
        allow_null=True,
    )

    # endregion

    # region BNTU

    bntu_positions = BntuPositionSerializer(many=True)

    # endregion

    # region TradeUnion

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
    exemption_ids = PrimaryKeyRelatedField(
        queryset=ExemptionModel.objects.all(), source="exemptions", many=True
    )

    # endregion

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["image_path"] = self._get_image_path(instance)
        representation.pop("image")
        return representation

    def _get_image_path(self, obj):
        if obj.image:
            return ImageSerializer(obj.image).data["file"]
        return None

    def create(self, validated_data):
        try:
            image = None
            image_path: str = validated_data.pop("image_path", None)

            print(image_path)

            if image_path:
                file = image_path.replace("/media/", "").replace("media/", "")

                print(file)

                print(file)
                image = ImageModel.objects.get(file=file)

            validated_data["image"] = image

            # Extract M2M and related data
            exemptions = validated_data.pop("exemptions", [])

            trade_union_department_path = validated_data.get(
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

            working_group = validated_data.get("working_group")
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
                "comments": CommentModel,
                "relatives": RelativeModel,
                "rewards": RewardModel,
            }
            related_data = {
                field: validated_data.pop(field, []) for field in model_map.keys()
            }

            employee_version = EmployeeVersionModel.objects.create(**validated_data)

            # Create related objects
            for field, data_list in related_data.items():
                model_class = model_map[field]
                for data in data_list:
                    model_class.objects.create(
                        employee_version=employee_version, **data
                    )

            # Now assign M2M
            employee_version.exemptions.set(exemptions)

            return employee_version

        except Exception as error:
            print(error)
            raise error

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
            "image",
            "image_path",
            "bntu_positions",
            "trade_union_membership_number",
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
            "created_at",
            "exemption_ids",
        )
        read_only_fields = [
            "working_group_authentic_label",
            "trade_union_department_authentic_label",
            "created_at",
        ]
