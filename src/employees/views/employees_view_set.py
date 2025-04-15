from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from rest_framework.response import Response

from ..utils.enumerations import Enumerations

from ..utils import EmployeeGenerator

from ..serializers import EmployeeSerializer, EmployeeVersionSerializer

from rest_framework.decorators import action

from ..models.employee_version_model import EmployeeModel, EmployeeVersionModel

from django.utils.dateparse import parse_datetime

from django.shortcuts import get_object_or_404

from rest_framework.pagination import PageNumberPagination


class EmployeesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "limit"


@permission_classes([IsAuthenticated])
class EmployeesViewSet(ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeesPagination

    @action(detail=True, methods=["get"], url_path=r"versions/(?P<created_at>.+)")
    def get_version_by_timestamp(self, request, pk: int, created_at: str):
        employee = self.queryset.get(pk=pk)
        try:
            dt = parse_datetime(created_at)
            if dt is None:
                return Response({"error": "Invalid timestamp format"}, status=400)

            version = get_object_or_404(
                EmployeeVersionModel.objects.filter(employee=employee), created_at=dt
            )
            serializer = EmployeeVersionSerializer(version)
            return Response(serializer.data)
        except ValueError:
            return Response({"error": "Invalid timestamp"}, status=400)

    @action(detail=True, methods=["post"], url_path=r"restore/(?P<created_at>.+)")
    def restore(self, request, pk: int, created_at: str):
        try:
            dt = parse_datetime(created_at)
            if dt is None:
                return Response({"error": "Invalid timestamp format"}, status=400)

            employee = self.queryset.get(pk=pk)
            version = (
                EmployeeVersionModel.objects.filter(
                    employee=employee, created_at__lte=dt
                )
                .order_by("-created_at")
                .first()
            )
            if not version:
                return Response(
                    {"error": "No version found at or before the specified timestamp"},
                    status=404,
                )

            EmployeeVersionModel.objects.filter(
                employee=employee, created_at__gt=dt
            ).delete()
            return Response(status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Invalid timestamp"}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

    @action(detail=False, methods=["post"], url_path="generate")
    def generate(self, request):
        return Response(
            self.get_serializer(EmployeeGenerator().generate()).data,
            status=status.HTTP_201_CREATED,
        )

    @action(detail=False, methods=["get"], url_path="enumerations")
    def enumerations(self, request):
        return Response(Enumerations.get())

    @action(detail=False, methods=["delete"], url_path="")
    def reset(self, request):
        try:
            EmployeeModel.objects.all().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {"error": f"Failed to delete records: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
