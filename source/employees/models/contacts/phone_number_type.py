from typing import TYPE_CHECKING
from django.db import models


from ...utils import Enumerated


if TYPE_CHECKING:
    from django.db.models import Manager
    from .phone_number import PhoneNumber


class PhoneNumberType(Enumerated):
    if TYPE_CHECKING:
        phone_numbers = Manager[PhoneNumber]
