from re import M
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from collections import defaultdict
from django.db.models.manager import BaseManager
from treebeard.mp_tree import MP_Node

from .serializers import (
    BntuDepartmentOptionSerializer,
    TradeUnionDepartmentOptionSerializer,
)
from .models import BntuDepartmentModel, TradeUnionDepartmentModel

TABLES = {
    "bntu_departments": (BntuDepartmentModel, BntuDepartmentOptionSerializer),
    "trade_union_departments": (
        TradeUnionDepartmentModel,
        TradeUnionDepartmentOptionSerializer,
    ),
}

POST_REQUEST_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "label": openapi.Schema(type=openapi.TYPE_STRING),
        "parent_path": openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=["label", "parent_path"],
)

PUT_REQUEST_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "label": openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=["label"],
)


class TreesAPIView(APIView):
    def get_model_and_serializer(self, table_name):
        if not table_name or table_name not in TABLES:
            raise Http404("Invalid or missing table_name")
        return TABLES[table_name]

    def get_queryset(self, model_class) -> BaseManager[MP_Node]:
        return model_class.objects.all()

    def get_object(self, model_class, path) -> MP_Node:
        try:
            return model_class.objects.get(path=path)
        except model_class.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "table_name",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description="Optional table name to retrieve specific table tree data",
            ),
        ],
    )
    def get(self, request):
        table_name = request.query_params.get("table_name")
        result = {}

        def build_tree(nodes, model_class, steplen):
            nodes_by_parent = defaultdict(list)
            for node in nodes:
                if len(node.path) > steplen:
                    parent_path = node.path[:-steplen]
                else:
                    parent_path = None
                nodes_by_parent[parent_path].append(node)

            def construct_tree(parent_path=None):
                children = []
                for node in nodes_by_parent.get(parent_path, []):
                    children.append(
                        {
                            "path": node.path,
                            "label": node.label,
                            "children": construct_tree(node.path),
                        }
                    )
                return children

            return construct_tree()

        if table_name:
            if table_name not in TABLES:
                return Response(
                    {"error": "Invalid table_name"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            model_class, _ = self.get_model_and_serializer(table_name)
            nodes = self.get_queryset(model_class)
            steplen = model_class.steplen
            result[table_name] = build_tree(nodes, model_class, steplen)
        else:
            for table_name, (model_class, _) in TABLES.items():
                nodes = self.get_queryset(model_class)
                steplen = model_class.steplen
                result[table_name] = build_tree(nodes, model_class, steplen)

        return Response(result)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "table_name", openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True
            ),
        ],
        request_body=POST_REQUEST_BODY,
    )
    def post(self, request):
        table_name = request.query_params.get("table_name")
        try:
            model_class, serializer_class = self.get_model_and_serializer(table_name)
        except Http404:
            return Response(
                {"error": "Invalid or missing table_name"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        parent_path = request.data.get("parent_path")
        label = request.data.get("label")

        try:
            if parent_path:
                parent = model_class.objects.get(path=parent_path)
                new_node = parent.add_child(label=label)
            else:
                new_node = model_class.add_root(label=label)
        except model_class.DoesNotExist:
            return Response(
                {"error": f"Parent node with path {parent_path} not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = serializer_class(new_node)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "table_name", openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True
            ),
            openapi.Parameter(
                "path", openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True
            ),
        ],
        request_body=PUT_REQUEST_BODY,
    )
    def put(self, request):
        table_name = request.query_params.get("table_name")
        path = request.query_params.get("path")

        try:
            model_class, serializer_class = self.get_model_and_serializer(table_name)
        except Http404:
            return Response(
                {"error": "Invalid or missing table_name"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not path:
            return Response(
                {"error": "Missing path parameter"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            instance = self.get_object(model_class, path)
        except Http404:
            return Response(
                {"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = serializer_class(instance, data=request.data, partial=True)
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
                "path", openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True
            ),
        ],
    )
    def delete(self, request):
        table_name = request.query_params.get("table_name")
        path = request.query_params.get("path")

        try:
            model_class, _ = self.get_model_and_serializer(table_name)
        except Http404:
            return Response(
                {"error": "Invalid or missing table_name"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not path:
            return Response(
                {"error": "Missing path parameter"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            instance = self.get_object(model_class, path)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response(
                {"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND
            )
