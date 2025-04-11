from re import M
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response

from ..serializers import (
    TreeSerializer,
    BntuDepartmentOptionSerializer,
    TradeUnionDepartmentOptionSerializer,
)
from ..models import BntuDepartmentOptionModel, TradeUnionDepartmentOptionModel

from collections import defaultdict
from treebeard.mp_tree import MP_Node
from django.db.models.manager import BaseManager


class TreeViewSet(viewsets.ModelViewSet):
    model_class: type[MP_Node]
    serializer_class = type[TreeSerializer]
    lookup_field = "path"

    def get_queryset(self) -> BaseManager[MP_Node]:  # type: ignore
        return self.model_class.objects.all()

    def get_object(self) -> MP_Node:  # type: ignore
        path = self.kwargs["path"]
        try:
            return self.model_class.objects.get(path=path)
        except self.model_class.DoesNotExist:
            raise Http404

    def list(self, request):
        nodes = self.model_class.objects.all()
        steplen = self.model_class.steplen

        nodes_by_parent = defaultdict(list)

        for node in nodes:
            if len(node.path) > steplen:
                parent_path = node.path[:-steplen]
            else:
                parent_path = None

            nodes_by_parent[parent_path].append(node)

        # Recursive function to build tree
        def build_tree(parent_path=None):
            children = []
            for node in nodes_by_parent.get(parent_path, []):
                children.append(
                    {
                        "path": node.path,
                        "label": node.label,
                        "children": build_tree(node.path),
                    }
                )
            return children

        tree_data = build_tree()
        return Response(tree_data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        parent_path = request.data.get("path")
        label = request.data["label"]

        try:
            if parent_path:
                parent = self.model_class.objects.get(path=parent_path)
                new_node = parent.add_child(label=label)
            else:
                new_node = self.model_class.add_root(label=label)
        except self.model_class.DoesNotExist:
            return Response(
                {"error": f"Parent node with path {parent_path} not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(new_node)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BntuDepartmentViewSet(TreeViewSet):
    model_class = BntuDepartmentOptionModel
    serializer_class = BntuDepartmentOptionSerializer


class TradeUnionDepartmentViewSet(TreeViewSet):
    model_class = TradeUnionDepartmentOptionModel
    serializer_class = TradeUnionDepartmentOptionSerializer
