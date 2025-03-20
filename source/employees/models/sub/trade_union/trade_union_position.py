from typing import TYPE_CHECKING
from django.db import models

from source.employees.models import Employee
from .working_group import WorkingGroup

if TYPE_CHECKING:
    from .trade_union_department import TradeUnionDepartment


class TradeUnionPosition(models.Model):
    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="trade_union_positions"
    )

    name = models.CharField(max_length=64)

    if TYPE_CHECKING:
        department: TradeUnionDepartment
        working_group: WorkingGroup

    joinedAt = models.DateTimeField(null=True)
    leftAt = models.DateTimeField(null=True)
