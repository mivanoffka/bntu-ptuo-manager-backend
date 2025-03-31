from typing import TYPE_CHECKING
from django.db import models


from ..abstract import EnumeratedModel


if TYPE_CHECKING:
    from django.db.models import Manager
    from .phone_number_model import PhoneNumberModel


class PhoneNumberTypeModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "phone_number_types"

    if TYPE_CHECKING:
        phone_numbers = Manager[PhoneNumberModel]
