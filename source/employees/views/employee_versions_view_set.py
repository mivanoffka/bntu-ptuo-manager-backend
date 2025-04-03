from rest_framework.viewsets import ModelViewSet

from ..serializers.employee_version_serializer import EmployeeSerializer

from ..models.employee_model import EmployeeVersionModel


class EmployeeVersionViewSet(ModelViewSet):
    queryset = EmployeeVersionModel.objects.all()
    serializer_class = EmployeeSerializer
