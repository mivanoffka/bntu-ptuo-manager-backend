from typing import TYPE_CHECKING
from django.db import models


from ...utils import Enumerated


if TYPE_CHECKING:
    from django.db.models import Manager
    from .relative import Relative


class RelativeType(Enumerated):
    class Meta(Enumerated.Meta):
        db_table = "relative_types"

    if TYPE_CHECKING:
        relatives = Manager[Relative]
