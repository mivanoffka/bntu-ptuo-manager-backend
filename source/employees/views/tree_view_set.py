# from rest_framework import viewsets
# from ..models import BntuDepartmentOptionModel
# from ..serializers import BntuDepartmentOptionSerializer


# class BntuDepartmentOptionViewSet(viewsets.ModelViewSet):
#     serializer_class = BntuDepartmentOptionSerializer
#     lookup_field = "path"

#     def get_queryset(self):
#         if self.action == "list":
#             return BntuDepartmentOptionModel.get_root_nodes()
#         else:
#             return BntuDepartmentOptionModel.objects.all()


from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import BntuDepartmentOptionModel
from ..serializers import BntuDepartmentOptionSerializer
from collections import defaultdict


class BntuDepartmentOptionViewSet(viewsets.ModelViewSet):
    serializer_class = BntuDepartmentOptionSerializer
    lookup_field = "path"  # Use 'path' instead of 'id' for lookups

    def get_queryset(self):
        return BntuDepartmentOptionModel.objects.all()

    def get_object(self):
        # Find node by path instead of ID
        path = self.kwargs["path"]
        try:
            return BntuDepartmentOptionModel.objects.get(path=path)
        except BntuDepartmentOptionModel.DoesNotExist:
            raise Http404

    def list(self, request):
        nodes = BntuDepartmentOptionModel.objects.all()
        steplen = BntuDepartmentOptionModel.steplen  # Typically 4 for MP_Node

        # Create a dictionary to hold nodes by their parent path
        nodes_by_parent = defaultdict(list)

        for node in nodes:
            # Get parent path by removing last steplen characters
            if len(node.path) > steplen:
                parent_path = node.path[:-steplen]
            else:
                parent_path = None  # Root node

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
                parent = BntuDepartmentOptionModel.objects.get(path=parent_path)
                new_node = parent.add_child(label=label)
            else:
                new_node = BntuDepartmentOptionModel.add_root(label=label)
        except BntuDepartmentOptionModel.DoesNotExist:
            return Response(
                {"error": f"Parent node with path {parent_path} not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(new_node)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
