from rest_framework import serializers
from .models import (
    ExemptionModel,
    GenderModel,
    WorkingGroupModel,
    RelativeTypeModel,
    AcademicDegreeModel,
    EducationLevelModel,
    PhoneNumberTypeModel,
)


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "label"]
        abstract = True


class GenderSerializer(ReferenceSerializer):
    class Meta(ReferenceSerializer.Meta):
        model = GenderModel


class WorkingGroupSerializer(ReferenceSerializer):
    class Meta(ReferenceSerializer.Meta):
        model = WorkingGroupModel
        fields = ["id", "label"]


class RelativeTypeSerializer(ReferenceSerializer):
    class Meta(ReferenceSerializer.Meta):
        model = RelativeTypeModel


class AcademicDegreeSerializer(ReferenceSerializer):
    class Meta(ReferenceSerializer.Meta):
        model = AcademicDegreeModel


class EducationLevelSerializer(ReferenceSerializer):
    class Meta(ReferenceSerializer.Meta):
        model = EducationLevelModel


class PhoneNumberTypeSerializer(ReferenceSerializer):
    class Meta(ReferenceSerializer.Meta):
        model = PhoneNumberTypeModel


class ExemptionSerializer(ReferenceSerializer):
    class Meta(ReferenceSerializer.Meta):
        model = ExemptionModel
