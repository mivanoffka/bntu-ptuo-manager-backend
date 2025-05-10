from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .access_policy import ReferencesAccessPolicy
from .models import (
    GenderModel,
    PhoneNumberTypeModel,
    EducationLevelModel,
    AcademicDegreeModel,
    WorkingGroupModel,
    RelativeTypeModel,
)
from .serializers import (
    GenderSerializer,
    PhoneNumberTypeSerializer,
    EducationLevelSerializer,
    AcademicDegreeSerializer,
    WorkingGroupSerializer,
    RelativeTypeSerializer,
)

TABLES = {
    "genders": (GenderModel, GenderSerializer),
    "phone_number_types": (PhoneNumberTypeModel, PhoneNumberTypeSerializer),
    "education_levels": (EducationLevelModel, EducationLevelSerializer),
    "academic_degrees": (AcademicDegreeModel, AcademicDegreeSerializer),
    "working_groups": (WorkingGroupModel, WorkingGroupSerializer),
    "relative_types": (RelativeTypeModel, RelativeTypeSerializer),
}

REQUEST_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={"label": openapi.Schema(type=openapi.TYPE_STRING)},
    required=["label"],
)


class ReferencesViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    access_policy = ReferencesAccessPolicy()

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "table_name",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description="Optional table name to retrieve specific table data",
            )
        ]
    )
    def list(self, request):
        table_name = request.query_params.get("table_name")
        result = {}

        if table_name:
            if table_name not in TABLES:
                return Response(
                    {"error": "Invalid table_name"}, status=status.HTTP_400_BAD_REQUEST
                )
            model_class, serializer_class = TABLES[table_name]
            queryset = model_class.objects.all()
            serializer = serializer_class(queryset, many=True)
            result[table_name] = serializer.data
        else:
            for name, (model_class, serializer_class) in TABLES.items():
                queryset = model_class.objects.all()
                serializer = serializer_class(queryset, many=True)
                result[name] = serializer.data

        return Response(result)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "table_name", openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True
            )
        ],
        request_body=REQUEST_BODY,
    )
    def create(self, request):
        table_name = request.query_params.get("table_name")
        label = request.data.get("label")

        if not table_name or table_name not in TABLES:
            return Response(
                {"error": "Invalid or missing table_name"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        model_class, serializer_class = TABLES[table_name]
        serializer = serializer_class(data={"label": label})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "table_name", openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True
            ),
            openapi.Parameter(
                "id", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True
            ),
        ],
        request_body=REQUEST_BODY,
    )
    def update(self, request, pk=None):
        table_name = request.query_params.get("table_name")
        obj_id = request.query_params.get("id")
        label = request.data.get("label")

        if not table_name or table_name not in TABLES:
            return Response(
                {"error": "Invalid or missing table_name"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not obj_id:
            return Response(
                {"error": "Missing id parameter"}, status=status.HTTP_400_BAD_REQUEST
            )

        model_class, serializer_class = TABLES[table_name]
        try:
            instance = model_class.objects.get(pk=obj_id)
        except model_class.DoesNotExist:
            return Response(
                {"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = serializer_class(instance, data={"label": label}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "table_name", openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True
            ),
            openapi.Parameter(
                "id", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True
            ),
        ]
    )
    def destroy(self, request, pk=None):
        table_name = request.query_params.get("table_name")
        obj_id = request.query_params.get("id")

        if not table_name or table_name not in TABLES:
            return Response(
                {"error": "Invalid or missing table_name"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not obj_id:
            return Response(
                {"error": "Missing id parameter"}, status=status.HTTP_400_BAD_REQUEST
            )

        model_class, _ = TABLES[table_name]
        try:
            instance = model_class.objects.get(pk=obj_id)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except model_class.DoesNotExist:
            return Response(
                {"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND
            )
