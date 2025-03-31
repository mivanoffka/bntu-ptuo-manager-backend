import datetime
from typing import Generic, Optional, Tuple, TypeVar
from rest_framework import serializers


T = TypeVar("T")


class HistoryItem(Generic[T]):
    _item: T
    _altered_at: Optional[datetime.datetime]

    def serialize(self, serializer: type[serializers.ModelSerializer]):
        return {"item": serializer(self._item).data, "altered_at": self._altered_at}

    @property
    def item(self):
        return self._item

    @property
    def altered_at(self):
        return self._altered_at

    def __init__(self, item: T, altered_at: Optional[datetime.datetime]):
        self._altered_at = altered_at if altered_at else None
        self._item = item
