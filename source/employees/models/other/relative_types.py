from typing import TYPE_CHECKING
from django.db import models


from ...utils import Enumerated


if TYPE_CHECKING:
    from django.db.models import Manager
    from .relative import Relative


class RelativeType(Enumerated):
    if TYPE_CHECKING:
        relatives = Manager[Relative]
