from typing import Generic, Optional, Tuple, TypeVar
from .history_item import HistoryItem
from .timestamp import Timestamped
from django.db.models import QuerySet
from rest_framework import serializers


T = TypeVar("T", bound=Timestamped)


class History(Generic[T]):
    _history: Tuple[HistoryItem[T]]
    _relevant: Optional[T]

    @property
    def history(self):
        return self._history

    @property
    def relevant(self):
        return self._relevant

    def __init__(
        self, history: Tuple[HistoryItem[T]], relevant: Optional[T] = None
    ) -> None:
        self._history = history
        self._relevant = relevant

    @staticmethod
    def to_timestamped(): ...

    @staticmethod
    def from_timestamped(
        objects: QuerySet[T],
        serializer: type[serializers.ModelSerializer],
        column_name: str = "created_at",
    ):
        items = sorted(
            objects.all(), key=lambda x: (x.created_at is None, x.created_at)
        )

        if not items:
            return {"items": [], "relevant": None}

        relevant = items[len(items) - 1]
        items = items[:-1]

        history_items = []
        for i, current in enumerate(items):
            next_item = items[i + 1] if i + 1 < len(items) else relevant
            altered_at = getattr(next_item, column_name)

            history_items.append(HistoryItem[T](serializer(current).data, altered_at))

        relevant_item = serializer(relevant).data

        return {"items": history_items, "relevant": relevant_item}

    @staticmethod
    def empty():
        return {"items": [], "relevant": None}
