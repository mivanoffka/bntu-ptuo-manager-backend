from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers import (
    AcademicDegreeSerializer,
    EducationLevelSerializer,
    GenderSerializer,
    PhoneNumberTypeSerializer,
    WorkingGroupOptionSerializer,
    RelativeTypeSerializer,
)

from ..models import (
    PhoneNumberType,
    Gender,
    AcademicDegree,
    EducationLevel,
    WorkingGroup,
    RelativeType,
)


class EnumerationsView(APIView):
    def _get_all_enums(
        self,
    ):
        return {
            "genders": [GenderSerializer(item).data for item in Gender.objects.all()],
            "phone_number_types": [
                PhoneNumberTypeSerializer(item).data
                for item in PhoneNumberType.objects.all()
            ],
            "education_level": [
                EducationLevelSerializer(item).data
                for item in EducationLevel.objects.all()
            ],
            "academic_degrees": [
                AcademicDegreeSerializer(item).data
                for item in AcademicDegree.objects.all()
            ],
            "working_groups": [
                WorkingGroupOptionSerializer(item).data
                for item in WorkingGroup.objects.all()
            ],
            "relative_types": [
                RelativeTypeSerializer(item).data for item in RelativeType.objects.all()
            ],
        }

    def get(self, request):
        return Response(self._get_all_enums())
