from typing import TYPE_CHECKING
from django.db import models


if TYPE_CHECKING:
    from django.db.models import Manager
    from .trade_union_position import TradeUnionPosition


class TradeUnionPositionName(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=64)

    if TYPE_CHECKING:
        entrances = Manager[TradeUnionPosition]
