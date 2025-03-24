from typing import TYPE_CHECKING
from django.db import models
from treebeard.mp_tree import MP_Node


if TYPE_CHECKING:
    from .trade_union_position import TradeUnionPosition
    from django.db.models import Manager


class TradeUnionDepartment(MP_Node):
    label = models.CharField(max_length=255)

    node_order_by = ["label"]

    def __str__(self):
        return self.label

    if TYPE_CHECKING:
        trade_union_positions: Manager[TradeUnionPosition]
