from typing import TYPE_CHECKING
from django.db import models


from ...utils import Enumerated


if TYPE_CHECKING:
    from django.db.models import Manager
    from .trade_union_position import TradeUnionPosition


class WorkingGroup(Enumerated):
    if TYPE_CHECKING:
        positions = Manager[TradeUnionPosition]
