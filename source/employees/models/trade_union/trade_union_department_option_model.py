from typing import TYPE_CHECKING

from ..abstract import TreeNodeModel

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager
    from .trade_union_department_record_model import TradeUnionDepartmentRecordModel


class TradeUnionDepartmentOptionModel(TreeNodeModel):
    class Meta(TreeNodeModel.Meta):
        db_table = "trade_union_department_options"

    if TYPE_CHECKING:
        trade_union_department_records: RelatedManager[TradeUnionDepartmentRecordModel]
