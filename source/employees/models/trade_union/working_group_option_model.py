from typing import TYPE_CHECKING
from django.db import models


from ..abstract import EnumeratedModel


if TYPE_CHECKING:
    from .working_group_record_model import WorkingGroupRecordModel
    from django.db.models.manager import RelatedManager


class WorkingGroupOptionModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "working_group_options"

    if TYPE_CHECKING:
        working_group_records = RelatedManager[WorkingGroupRecordModel]
