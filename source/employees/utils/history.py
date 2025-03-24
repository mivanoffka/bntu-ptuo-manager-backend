from typing import Generic, Optional, Tuple, TypeVar
from .history_item import HistoryItem
from .timestamp import Timestamped
from django.db.models import QuerySet
from rest_framework import serializers


T = TypeVar("T", bound=Timestamped)


class BaseHistory(Generic[T]):
    _history: Tuple[HistoryItem[T], ...]
    _relevant: Optional[T]

    @property
    def history(self):
        return self._history

    @property
    def relevant(self):
        return self._relevant

    def __init__(
        self, history: Tuple[HistoryItem[T], ...], relevant: Optional[T] = None
    ) -> None:
        self._history = history
        self._relevant = relevant

    def serialize(self, serializer: type[serializers.ModelSerializer]):
        return {
            "history": (item.serialize(serializer) for item in self._history),
            "relevant": serializer(self._relevant).data,
        }


class History(BaseHistory, Generic[T]):
    @staticmethod
    def empty():
        return BaseHistory((), None)

    @staticmethod
    def to_timestamped(): ...

    @staticmethod
    def from_timestamped(
        objects: QuerySet[T],
        column_name: str = "created_at",
    ):
        items = sorted(
            objects.all(), key=lambda x: (x.created_at is None, x.created_at)
        )

        if not items:
            return History.empty()

        relevant = items[len(items) - 1]
        items = items[:-1]

        history_items = []
        for i, current in enumerate(items):
            next_item = items[i + 1] if i + 1 < len(items) else relevant
            altered_at = getattr(next_item, column_name)

            history_items.append(HistoryItem[T](current, altered_at))

        return BaseHistory(tuple(history_items), relevant)
