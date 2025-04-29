from ...models import RelativeTypeModel
from ..generic import EnumeratedSerializer


class RelativeTypeSerializer(EnumeratedSerializer):
    class Meta(EnumeratedSerializer.Meta):
        model = RelativeTypeModel
