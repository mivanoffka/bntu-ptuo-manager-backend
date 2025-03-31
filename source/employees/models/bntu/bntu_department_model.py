from typing import TYPE_CHECKING

from django.db import models
from treebeard.mp_tree import MP_Node

if TYPE_CHECKING:
    from .bntu_position_model import BntuPositionModel
    from django.db.models import Manager


class BntuDepartmentModel(MP_Node):
    class Meta(MP_Node.Meta):
        db_table = "bntu_departments"

    label = models.CharField(max_length=255)

    node_order_by = ["label"]

    def __str__(self):
        return self.label

    if TYPE_CHECKING:
        bntu_positions = Manager[BntuPositionModel]
