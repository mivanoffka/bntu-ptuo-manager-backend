from rest_framework.viewsets import ModelViewSet

from ..serializers.employee_version_serializer import EmployeeVersionSerializer

from ..models.employee_version_model import EmployeeVersionModel


class EmployeeVersionViewSet(ModelViewSet):
    queryset = EmployeeVersionModel.objects.all()
    serializer_class = EmployeeVersionSerializer
