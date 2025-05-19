from django.db import models

from treebeard.mp_tree import MP_Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from employees.models import BntuPositionModel, EmployeeVersionModel
    from django.db.models.manager import RelatedManager


class TreeNodeModel(MP_Node):
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=255, unique=True)
    label = models.CharField(max_length=255)
    node_order_by = []

    def __str__(self):
        return self.label

    class Meta(MP_Node.Meta):
        abstract = True


class BntuDepartmentModel(TreeNodeModel):
    class Meta(TreeNodeModel.Meta):
        db_table = "bntu_departments"

    if TYPE_CHECKING:
        bntu_positions = RelatedManager[BntuPositionModel]


class TradeUnionDepartmentModel(TreeNodeModel):
    class Meta(TreeNodeModel.Meta):
        db_table = "trade_union_departments"

    if TYPE_CHECKING:
        employee_versions: RelatedManager[EmployeeVersionModel]
