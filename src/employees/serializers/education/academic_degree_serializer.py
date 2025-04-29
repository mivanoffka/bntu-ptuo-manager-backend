from ...models import AcademicDegreeModel
from ..generic import EnumeratedSerializer


class AcademicDegreeSerializer(EnumeratedSerializer):
    class Meta(EnumeratedSerializer.Meta):
        model = AcademicDegreeModel
