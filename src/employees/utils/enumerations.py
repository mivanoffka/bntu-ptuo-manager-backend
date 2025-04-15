from ..models import (
    PhoneNumberTypeModel,
    GenderModel,
    AcademicDegreeModel,
    EducationLevelModel,
    RelativeTypeModel,
    WorkingGroupOptionModel,
    BntuDepartmentOptionModel,
    TradeUnionDepartmentOptionModel,
)

from ..serializers import EnumeratedSerializer, TreeNodeSerializer


class Enumerations:
    @staticmethod
    def get():
        return {
            "genders": [
                EnumeratedSerializer(item).data for item in GenderModel.objects.all()
            ],
            "phone_number_types": [
                EnumeratedSerializer(item).data
                for item in PhoneNumberTypeModel.objects.all()
            ],
            "education_levels": [
                EnumeratedSerializer(item).data
                for item in EducationLevelModel.objects.all()
            ],
            "academic_degrees": [
                EnumeratedSerializer(item).data
                for item in AcademicDegreeModel.objects.all()
            ],
            "working_groups": [
                EnumeratedSerializer(item).data
                for item in WorkingGroupOptionModel.objects.all()
            ],
            "relative_types": [
                EnumeratedSerializer(item).data
                for item in RelativeTypeModel.objects.all()
            ],
        }
