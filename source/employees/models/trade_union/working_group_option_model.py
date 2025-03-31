from typing import TYPE_CHECKING
from django.db import models


from ..abstract import EnumeratedModel


if TYPE_CHECKING:
    from .working_group_model import WorkingGroupModel
    from django.db.models import Manager


class WorkingGroupOptionModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "working_group_options"

    if TYPE_CHECKING:
        working_groups = Manager[WorkingGroupModel]
