from ...models import GenderModel
from ..generic import EnumeratedSerializer


class GenderSerializer(EnumeratedSerializer):
    class Meta(EnumeratedSerializer.Meta):
        model = GenderModel
