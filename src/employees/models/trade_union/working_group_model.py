from typing import TYPE_CHECKING
from django.db import models


from ..abstract import EnumeratedModel


if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager
    from ..employee_version_model import EmployeeVersionModel


class WorkingGroupModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "working_group_options"

    if TYPE_CHECKING:
        employee_versions: RelatedManager[EmployeeVersionModel]
