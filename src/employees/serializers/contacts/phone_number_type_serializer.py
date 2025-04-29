from ...models import PhoneNumberTypeModel
from ..generic import EnumeratedSerializer


class PhoneNumberTypeSerializer(EnumeratedSerializer):
    class Meta(EnumeratedSerializer.Meta):
        model = PhoneNumberTypeModel
