from typing import TYPE_CHECKING
from django.db import models

from ..utils import Enumerated


if TYPE_CHECKING:
    from django.db.models import Manager
    from .employee import Employee


class Gender(Enumerated):
    if TYPE_CHECKING:
        employees = Manager[Employee]
