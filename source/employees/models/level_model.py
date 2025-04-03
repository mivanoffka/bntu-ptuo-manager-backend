from typing import TYPE_CHECKING
from django.db import models

from .abstract import EnumeratedModel


if TYPE_CHECKING:
    from django.db.models import Manager
    from .employee_model import EmployeeVersionModel


class EducationLevelModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "education_levels"

    if TYPE_CHECKING:
        employees = Manager[EmployeeVersionModel]
