from rest_framework.viewsets import ModelViewSet

from ..serializers.employee_serializer import EmployeeSerializer

from ..models.employee_model import EmployeeModel


class EmployeeView(ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
