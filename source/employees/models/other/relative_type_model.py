from typing import TYPE_CHECKING
from django.db import models


from ..abstract import EnumeratedModel


if TYPE_CHECKING:
    from django.db.models import Manager
    from .relative_model import RelativeModel


class RelativeTypeModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "relative_types"

    if TYPE_CHECKING:
        relatives = Manager[RelativeModel]
