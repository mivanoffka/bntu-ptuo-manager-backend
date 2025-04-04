from rest_framework.viewsets import ModelViewSet

from ..serializers import EmployeeSerializer

from ..models.employee_version_model import EmployeeModel


class EmployeesViewSet(ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
