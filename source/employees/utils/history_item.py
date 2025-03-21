import datetime
from typing import Generic, Optional, Tuple, TypeVar

T = TypeVar("T")


class HistoryItem(Generic[T]):
    _item: T
    _altered_at: Optional[datetime.datetime]

    def __init__(self, item: T, altered_at: Optional[datetime.datetime]):
        self._altered_at = altered_at if altered_at else None
        self._item = item
