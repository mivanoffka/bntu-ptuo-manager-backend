from ...models import WorkingGroupModel
from ..generic import EnumeratedSerializer


class WorkingGroupSerializer(EnumeratedSerializer):
    class Meta(EnumeratedSerializer.Meta):
        model = WorkingGroupModel
        fields = ["id", "label"]
