from typing import TYPE_CHECKING
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from source.employees.models import Employee

if TYPE_CHECKING:
    from django.db.models import Manager
    from .trade_union_position import TradeUnionPosition


class WorkingGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    positions = models.ForeignKey(
        TradeUnionPosition, on_delete=models.CASCADE, related_name="working_group"
    )
