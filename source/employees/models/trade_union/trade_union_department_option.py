from typing import TYPE_CHECKING
from django.db import models
from treebeard.mp_tree import MP_Node

if TYPE_CHECKING:
    from django.db.models import Manager
    from .trade_union_department import TradeUnionDepartment


class TradeUnionDepartmentOption(MP_Node):
    class Meta(MP_Node.Meta):
        db_table = "trade_union_department_options"

    label = models.CharField(max_length=255)

    node_order_by = ["label"]

    if TYPE_CHECKING:
        trade_union_departments: Manager[TradeUnionDepartment]

    def __str__(self):
        return self.label
