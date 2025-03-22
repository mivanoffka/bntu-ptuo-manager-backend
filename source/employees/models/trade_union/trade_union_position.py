from typing import TYPE_CHECKING
from django.db import models

from ..employee import Employee
from .working_group import WorkingGroup


if TYPE_CHECKING:
    from .trade_union_department import TradeUnionDepartment


class TradeUnionPosition(models.Model):
    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="trade_union_positions"
    )

    working_group = models.ForeignKey(
        WorkingGroup,
        on_delete=models.CASCADE,
        related_name="positions",
        null=True,
        blank=True,
    )

    name = models.CharField(max_length=64)

    if TYPE_CHECKING:
        department: TradeUnionDepartment

    joinedAt = models.DateTimeField(null=True, blank=True)
    leftAt = models.DateTimeField(null=True, blank=True)
