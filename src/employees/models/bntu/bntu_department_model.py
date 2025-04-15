from typing import TYPE_CHECKING

from ..abstract import TreeNodeModel

if TYPE_CHECKING:
    from .bntu_department_model import BntuDepartmentModel
    from django.db.models.manager import RelatedManager


class BntuDepartmentModel(TreeNodeModel):
    class Meta(TreeNodeModel.Meta):
        db_table = "bntu_departments"

    if TYPE_CHECKING:
        bntu_department_records = RelatedManager[BntuDepartmentModel]
