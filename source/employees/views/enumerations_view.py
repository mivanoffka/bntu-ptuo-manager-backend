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
    PhoneNumberTypeModel,
    GenderModel,
    AcademicDegreeModel,
    EducationLevelModel,
    WorkingGroupModel,
    RelativeTypeModel,
)


class EnumerationsView(APIView):
    def _get_all_enums(
        self,
    ):
        return {
            "genders": [
                GenderSerializer(item).data for item in GenderModel.objects.all()
            ],
            "phone_number_types": [
                PhoneNumberTypeSerializer(item).data
                for item in PhoneNumberTypeModel.objects.all()
            ],
            "education_level": [
                EducationLevelSerializer(item).data
                for item in EducationLevelModel.objects.all()
            ],
            "academic_degrees": [
                AcademicDegreeSerializer(item).data
                for item in AcademicDegreeModel.objects.all()
            ],
            "working_groups": [
                WorkingGroupOptionSerializer(item).data
                for item in WorkingGroupModel.objects.all()
            ],
            "relative_types": [
                RelativeTypeSerializer(item).data
                for item in RelativeTypeModel.objects.all()
            ],
        }

    def get(self, request):
        return Response(self._get_all_enums())
