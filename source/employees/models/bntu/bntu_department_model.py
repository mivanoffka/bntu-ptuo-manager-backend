from typing import TYPE_CHECKING

from ..abstract import TreeNodeModel

if TYPE_CHECKING:
    from .bntu_position_model import BntuPositionModel
    from django.db.models import Manager


class BntuDepartmentModel(TreeNodeModel):
    class Meta(TreeNodeModel.Meta):
        db_table = "bntu_departments"

    if TYPE_CHECKING:
        bntu_positions = Manager[BntuPositionModel]
