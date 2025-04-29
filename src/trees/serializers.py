from rest_framework import serializers
from treebeard.mp_tree import MP_Node

from .models import BntuDepartmentModel, TradeUnionDepartmentModel


class TreeSerializer(serializers.ModelSerializer):
    path = serializers.CharField(
        write_only=True,
        required=False,
        allow_null=True,
        help_text="The parent node's path. Omit to create a root node.",
    )
    node_path = serializers.CharField(source="path", read_only=True)

    class Meta:
        model: type[MP_Node]
        fields = ("node_path", "label", "path")
        read_only_fields = ("node_path",)

    def get_model(self):
        return self.Meta.model

    def create(self, validated_data):
        parent_path = validated_data.pop("path", None)
        label = validated_data.get("label")

        try:
            if parent_path:
                parent = self.get_model().objects.get(path=parent_path)
                new_node = parent.add_child(label=label)
            else:
                new_node = self.get_model().add_root(label=label)
        except self.get_model().DoesNotExist:
            raise serializers.ValidationError({"path": "Parent node not found."})

        return new_node


class BntuDepartmentOptionSerializer(TreeSerializer):
    class Meta(TreeSerializer.Meta):
        model = BntuDepartmentModel


class TradeUnionDepartmentOptionSerializer(TreeSerializer):
    class Meta(TreeSerializer.Meta):
        model = TradeUnionDepartmentModel
