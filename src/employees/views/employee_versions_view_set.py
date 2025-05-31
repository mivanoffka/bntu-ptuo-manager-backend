from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from rest_framework.decorators import action

from rest_framework.response import Response

from ..serializers.employee_serializer import EmployeeSerializer

from ..access_policies.employee_versions_access_policy import (
    EmployeeVersionsAccessPolicy,
)
from ..serializers import (
    EmployeeVersionSerializer,
)
from ..models.employee_version_model import EmployeeModel, EmployeeVersionModel
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound


class EmployeesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "limit"


@permission_classes([IsAuthenticated, EmployeeVersionsAccessPolicy])
class EmployeeVersionsViewSet(ModelViewSet):
    queryset = EmployeeVersionModel.objects.all()
    serializer_class = EmployeeVersionSerializer

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_object(self):
        queryset = self.get_queryset()
        created_at = self.kwargs.get("created_at")
        employee_id = self.kwargs.get("id")

        employee = EmployeeModel.objects.get(id=employee_id)

        try:
            return queryset.get(employee=employee, created_at=created_at)
        except EmployeeVersionModel.DoesNotExist:
            raise NotFound("Object not found.")

            return Response({"error": "Invalid timestamp"}, status=400)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @transaction.atomic
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=["patch"], url_path=r"/restore")
    def restore(self, request, *args, **kwargs):
        try:
            created_at = self.kwargs.get("created_at")
            employee_id = self.kwargs.get("id")

            with transaction.atomic():
                employee = EmployeeModel.objects.get(id=employee_id)
                version = (
                    EmployeeVersionModel.objects.filter(
                        employee=employee, created_at=created_at
                    )
                    .order_by("-created_at")
                    .first()
                )
                if not version:
                    return Response(
                        {
                            "error": "No version found at or before the specified timestamp"
                        },
                        status=404,
                    )

                EmployeeVersionModel.objects.filter(
                    employee=employee, created_at__gt=created_at
                ).delete()

                response_data = EmployeeSerializer(
                    EmployeeModel.objects.get(id=employee_id)
                ).data

                return Response(response_data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Invalid timestamp"}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
