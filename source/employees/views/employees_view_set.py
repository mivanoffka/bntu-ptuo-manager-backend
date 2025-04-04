from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from rest_framework.response import Response

from ..utils.enumerations import Enumerations

from ..utils import EmployeeGenerator

from ..serializers import EmployeeSerializer

from rest_framework.decorators import action

from ..models.employee_version_model import EmployeeModel


@permission_classes([IsAuthenticated])
class EmployeesViewSet(ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=False, methods=["post"], url_path="generate")
    def generate(self, request):
        return Response(
            self.get_serializer(EmployeeGenerator().generate()).data,
            status=status.HTTP_201_CREATED,
        )

    @action(detail=False, methods=["get"], url_path="enumerations")
    def enumerations(self, request):
        return Response(Enumerations.get())
