from typing import TYPE_CHECKING
from django.db import models

from .abstract import EnumeratedModel

if TYPE_CHECKING:
    from django.db.models import Manager
    from .employee_model import EmployeeModel


class AcademicDegree(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "academic_degrees"

    if TYPE_CHECKING:
        employees = Manager[EmployeeModel]
