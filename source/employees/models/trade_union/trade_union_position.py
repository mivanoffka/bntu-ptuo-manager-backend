from typing import TYPE_CHECKING
from django.db import models

from .trade_union_position_name import TradeUnionPositionName

from ..employee import Employee
from .working_group import WorkingGroup
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

    name = models.ForeignKey(
        TradeUnionPositionName,
        on_delete=models.CASCADE,
        related_name="positions",
        null=True,
        blank=True,
    )

    department = models.ForeignKey(
        TradeUnionDepartment,
        on_delete=models.CASCADE,
        related_name="positions",
        null=True,
        blank=True,
    )

    joined_at = models.DateTimeField(null=True, blank=True)
    left_at = models.DateTimeField(null=True, blank=True)
