from typing import TYPE_CHECKING
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from ..employee import Employee
from .trade_union_position import TradeUnionPosition


if TYPE_CHECKING:
    from django.db.models import Manager


class TradeUnionDepartment(MPTTModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    positions = models.ForeignKey(
        TradeUnionPosition, on_delete=models.CASCADE, related_name="department"
    )

    parent = TreeForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="children"
    )

    if TYPE_CHECKING:
        children: Manager["TradeUnionDepartment"]
