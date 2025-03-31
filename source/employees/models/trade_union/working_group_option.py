from typing import TYPE_CHECKING
from django.db import models


from ...utils import Enumerated


if TYPE_CHECKING:
    from .working_group import WorkingGroup
    from django.db.models import Manager


class WorkingGroupOption(Enumerated):
    class Meta(Enumerated.Meta):
        db_table = "working_group_options"

    if TYPE_CHECKING:
        working_groups = Manager[WorkingGroup]
