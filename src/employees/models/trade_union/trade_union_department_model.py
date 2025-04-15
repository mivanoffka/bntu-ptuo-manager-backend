from typing import TYPE_CHECKING

from ..abstract import TreeNodeModel

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager
    from ..employee_version_model import EmployeeVersionModel


class TradeUnionDepartmentModel(TreeNodeModel):
    class Meta(TreeNodeModel.Meta):
        db_table = "trade_union_departments"

    if TYPE_CHECKING:
        employee_versions: RelatedManager[EmployeeVersionModel]
