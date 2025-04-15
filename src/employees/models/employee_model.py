from __future__ import annotations
from typing import TYPE_CHECKING
from django.db import models

if TYPE_CHECKING:
    from .employee_version_model import EmployeeVersionModel
    from django.db.models.manager import RelatedManager


class EmployeeModel(models.Model):
    class Meta:
        db_table = "employees"

    id = models.AutoField(primary_key=True)

    if TYPE_CHECKING:
        employee_versions: RelatedManager[EmployeeVersionModel]
