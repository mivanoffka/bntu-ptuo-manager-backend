from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.response import Response

from .access_policy import EmployeesAccessPolicy

from .serializers.employee_version_plain_serializer import (
    EmployeeVersionPlainSerializer,
)

from .filters import EmployeeDynamicSearchFilter, EmployeeFilter

from .utils import EmployeeGenerator

from .serializers import (
    EmployeeSerializer,
    EmployeeVersionSerializer,
    GenerateEmployeesSerializer,
)

from rest_framework.decorators import action

from .models.employee_version_model import EmployeeModel, EmployeeVersionModel

from django.utils.dateparse import parse_datetime

from django.shortcuts import get_object_or_404

from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from datetime import datetime as Datetime

import pandas

from django.http import HttpResponse


class EmployeesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "limit"


@permission_classes([IsAuthenticated, EmployeesAccessPolicy])
class EmployeesViewSet(ModelViewSet):
    queryset = EmployeeModel.objects.all().prefetch_related(
        "employee_versions",
        "employee_versions__gender",
        "employee_versions__bntu_positions",
    )
    serializer_class = EmployeeSerializer
    pagination_class = EmployeesPagination
    filter_backends = (EmployeeDynamicSearchFilter, DjangoFilterBackend)
    filterset_class = EmployeeFilter

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "search_fields",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "birthdate_min",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
            ),
            openapi.Parameter(
                "birthdate_max",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
            ),
            openapi.Parameter(
                "gender_ids",
                openapi.IN_QUERY,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_INTEGER),
                collectionFormat="multi",
                explode=True,
            ),
            openapi.Parameter(
                "education_level_ids",
                openapi.IN_QUERY,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_INTEGER),
                collectionFormat="multi",
                explode=True,
            ),
            openapi.Parameter(
                "academic_degree_ids",
                openapi.IN_QUERY,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_INTEGER),
                collectionFormat="multi",
                explode=True,
            ),
            openapi.Parameter(
                "working_group_ids",
                openapi.IN_QUERY,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_INTEGER),
                collectionFormat="multi",
                explode=True,
            ),
            openapi.Parameter(
                "is_archived",
                openapi.IN_QUERY,
                type=openapi.TYPE_BOOLEAN,
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "search_fields",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "birthdate_min",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
            ),
            openapi.Parameter(
                "birthdate_max",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
            ),
            openapi.Parameter(
                "gender_ids",
                openapi.IN_QUERY,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_INTEGER),
                collectionFormat="multi",
                explode=True,
            ),
            openapi.Parameter(
                "education_level_ids",
                openapi.IN_QUERY,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_INTEGER),
                collectionFormat="multi",
                explode=True,
            ),
            openapi.Parameter(
                "academic_degree_ids",
                openapi.IN_QUERY,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_INTEGER),
                collectionFormat="multi",
                explode=True,
            ),
            openapi.Parameter(
                "working_group_ids",
                openapi.IN_QUERY,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_INTEGER),
                collectionFormat="multi",
                explode=True,
            ),
            openapi.Parameter(
                "is_archived",
                openapi.IN_QUERY,
                type=openapi.TYPE_BOOLEAN,
            ),
        ],
        responses={200: "Excel file with all employees"},
    )
    @action(detail=False, methods=["get"], url_path="export-excel")
    def export_excel(self, request):
        employees = self.filter_queryset(self.get_queryset())
        latest_versions = (
            EmployeeVersionPlainSerializer(employee.latest_version()).data
            for employee in employees
        )

        df_data = []
        for latest_version in latest_versions:
            last_name = latest_version.get("last_name", None)
            first_name = latest_version.get("first_name", None)
            middle_name = latest_version.get("middle_name", None)

            last_name += " " if last_name else None
            first_name += " " if first_name else None
            middle_name += " " if middle_name else None

            row = {
                "ФИО": f"{last_name}{first_name}{middle_name}"[:-1],
                "Дата рождения": latest_version.get("birthdate", ""),
                "Пол": (latest_version.get("gender")),
                "Ур. образования": (latest_version.get("education_level")),
                "Уч. степень": (latest_version.get("academic_degree")),
                "Профгруппа": (latest_version.get("working_group")),
                "Место работы": ", ".join(
                    [
                        pos.get("position", "") + " (" + pos.get("department", "") + ")"
                        for pos in latest_version.get("bntu_positions", [])
                    ][:-1]
                ),
            }
            df_data.append(row)

        # Create DataFrame
        df = pandas.DataFrame(df_data)

        # Create Excel file in memory
        output = pandas.ExcelWriter("employees.xlsx", engine="xlsxwriter")
        df.to_excel(output, sheet_name="Employees", index=False)
        output.close()

        # Prepare response
        with open("employees.xlsx", "rb") as excel_file:
            response = HttpResponse(
                excel_file.read(),
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            timestamp = Datetime.now().strftime("%Y%m%d_%H%M%S")
            response["Content-Disposition"] = (
                f"attachment; filename=employees_{timestamp}.xlsx"
            )

        return response

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

    @action(
        detail=True, methods=["delete"], url_path=r"versions/(?P<created_at>.+)/delete"
    )
    def delete_version_by_timestamp(self, request, pk: int, created_at: str):
        employee = self.queryset.get(pk=pk)
        try:
            dt = parse_datetime(created_at)
            if dt is None:
                return Response({"error": "Invalid timestamp format"}, status=400)

            version = get_object_or_404(
                EmployeeVersionModel.objects.filter(employee=employee), created_at=dt
            )

            version.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError:
            return Response({"error": "Invalid timestamp"}, status=400)

    @action(
        detail=True, methods=["post"], url_path=r"versions/(?P<created_at>.+)/restore"
    )
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

    @swagger_auto_schema(
        method="post",
        request_body=GenerateEmployeesSerializer,
        responses={201: EmployeeSerializer(many=True)},
    )
    @action(detail=False, methods=["post"], url_path="generate")
    def generate(self, request):
        serializer = GenerateEmployeesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        count = serializer.data.get("count", 1)

        employees = EmployeeGenerator().generate(count=count)
        return Response(
            self.get_serializer(employees, many=True).data,
            status=status.HTTP_201_CREATED,
        )

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
