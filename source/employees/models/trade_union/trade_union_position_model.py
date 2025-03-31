from typing import TYPE_CHECKING
from django.db import models

from ..employee_model import EmployeeModel


class TradeUnionPositionModel(models.Model):
    class Meta:
        db_table = "trade_union_positions"

    id = models.AutoField(primary_key=True)

    label = models.CharField(max_length=255)

    occurred_at = models.DateTimeField(null=True, blank=True)

    comment = models.TextField(null=True, blank=True, max_length=512)

    employee = models.ForeignKey(
        EmployeeModel, on_delete=models.CASCADE, related_name=Meta.db_table
    )
