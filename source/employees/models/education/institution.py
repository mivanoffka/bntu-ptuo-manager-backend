from typing import TYPE_CHECKING
from django.db import models

from ...utils import Enumerated


if TYPE_CHECKING:
    from ..employee import Employee


class EducationalInstitution(Enumerated):
    if TYPE_CHECKING:
        employees = models.ManyToManyField(
            Employee, related_name="educational_institutions"
        )
