from typing import TYPE_CHECKING

from ..abstract import TreeNodeModel

if TYPE_CHECKING:
    from .bntu_department_option_model import BntuDepartmentOptionModel
    from django.db.models.manager import RelatedManager


class BntuDepartmentOptionModel(TreeNodeModel):
    class Meta(TreeNodeModel.Meta):
        db_table = "bntu_department_options"

    if TYPE_CHECKING:
        bntu_department_records = RelatedManager[BntuDepartmentOptionModel]
