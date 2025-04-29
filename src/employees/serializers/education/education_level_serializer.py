from ...models import EducationLevelModel
from ..generic import EnumeratedSerializer


class EducationLevelSerializer(EnumeratedSerializer):
    class Meta(EnumeratedSerializer.Meta):
        model = EducationLevelModel
