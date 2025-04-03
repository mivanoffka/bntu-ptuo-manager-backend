from rest_framework.views import APIView
from rest_framework.response import Response


from ..models import (
    PhoneNumberTypeModel,
    GenderModel,
    AcademicDegreeModel,
    EducationLevelModel,
    RelativeTypeModel,
    WorkingGroupOptionModel,
    BntuDepartmentModel,
    TradeUnionDepartmentOptionModel,
)

from ..serializers import EnumeratedSerializer, TreeNodeSerializer


class EnumerationsView(APIView):
    def _get_all_enums(
        self,
    ):
        return {
            "genders": [
                EnumeratedSerializer(item).data for item in GenderModel.objects.all()
            ],
            "phone_number_types": [
                EnumeratedSerializer(item).data
                for item in PhoneNumberTypeModel.objects.all()
            ],
            "education_level": [
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
            "bntu_departments": [
                TreeNodeSerializer(item).data
                for item in BntuDepartmentModel.objects.all()
            ],
            "trade_union_department_options": [
                TreeNodeSerializer(item).data
                for item in TradeUnionDepartmentOptionModel.objects.all()
            ],
        }

    def get(self, request):
        return Response(self._get_all_enums())
