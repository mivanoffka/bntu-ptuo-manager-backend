from rest_framework import serializers

from ...models.abstract.tree_node_model import TreeNodeModel


class TreeNodeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    label = serializers.CharField()
    path = serializers.CharField()
    hierarchy = serializers.SerializerMethodField()

    def get_hierarchy(self, obj: TreeNodeModel):
        return [ancestor.label for ancestor in obj.get_ancestors().all()]  # type: ignore
