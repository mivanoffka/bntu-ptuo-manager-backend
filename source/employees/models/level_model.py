from typing import TYPE_CHECKING
from django.db import models

from .abstract import EnumeratedModel


if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager
    from .employee_version_model import EmployeeVersionModel


class EducationLevelModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "education_levels"

    if TYPE_CHECKING:
        employees: RelatedManager[EmployeeVersionModel]
