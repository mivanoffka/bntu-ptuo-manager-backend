# from rest_framework import serializers
# from ..models import BntuDepartmentOptionModel


# class BntuDepartmentOptionSerializer(serializers.ModelSerializer):
#     parent_path = serializers.CharField(write_only=True, required=False)
#     children = serializers.SerializerMethodField()

#     class Meta:
#         model = BntuDepartmentOptionModel
#         fields = ["path", "label", "children", "parent_path"]
#         read_only_fields = ["path", "children"]

#     def get_children(self, obj):
#         return BntuDepartmentOptionSerializer(obj.get_children(), many=True).data

#     def create(self, validated_data):
#         parent_path = validated_data.pop("parent_path", None)
#         if parent_path:
#             try:
#                 parent = BntuDepartmentOptionModel.objects.get(path=parent_path)
#                 node = parent.add_child(**validated_data)
#             except BntuDepartmentOptionModel.DoesNotExist:
#                 raise serializers.ValidationError("Parent node not found")
#         else:
#             node = BntuDepartmentOptionModel.add_root(**validated_data)
#         return node

from rest_framework import serializers
from ..models import BntuDepartmentOptionModel


class BntuDepartmentOptionSerializer(serializers.ModelSerializer):
    path = serializers.CharField(
        write_only=True,
        required=False,
        allow_null=True,
        help_text="The parent node's path. Omit to create a root node.",
    )
    node_path = serializers.CharField(source="path", read_only=True)

    class Meta:
        model = BntuDepartmentOptionModel
        fields = ("node_path", "label", "path")
        read_only_fields = ("node_path",)

    def create(self, validated_data):
        parent_path = validated_data.pop("path", None)
        label = validated_data.get("label")

        try:
            if parent_path:
                parent = BntuDepartmentOptionModel.objects.get(path=parent_path)
                new_node = parent.add_child(label=label)
            else:
                new_node = BntuDepartmentOptionModel.add_root(label=label)
        except BntuDepartmentOptionModel.DoesNotExist:
            raise serializers.ValidationError({"path": "Parent node not found."})

        return new_node
