from typing import TYPE_CHECKING
from django.db import models

from .abstract import EnumeratedModel


if TYPE_CHECKING:
    from django.db.models import Manager
    from .employee_model import EmployeeVersionModel


class GenderModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "genders"

    if TYPE_CHECKING:
        employees = Manager[EmployeeVersionModel]
