from typing import TYPE_CHECKING
from django.db import models

from .parts import Gender, EducationLevels, AcademicDegrees


if TYPE_CHECKING:
    from django.db.models import Manager
    from .parts import (
        Name,
        BntuPosition,
        PhoneNumber,
        Address,
        Email,
        TradeUnionPosition,
        Reward,
        Relative,
        Comment,
        EducationalInstitution,
    )


class Employee(models.Model):
    # region Common

    if TYPE_CHECKING:
        names: Manager[Name]

    id = models.AutoField(primary_key=True)

    birthdate = models.DateField()
    birthplace = models.CharField(max_length=256)

    gender = models.IntegerField(
        choices=Gender.choices,
        default=None,
        null=True,
        blank=True,
    )

    # endregion

    # region BNTU

    if TYPE_CHECKING:
        bntu_positions: Manager[BntuPosition]

    # endregion

    # region Trade union

    if TYPE_CHECKING:
        trade_union_positions: Manager[TradeUnionPosition]

    joined_at = models.DateTimeField(null=True)
    is_archived = models.BooleanField(default=False)
    archived_at = models.DateTimeField(null=True, blank=True)
    is_retired = models.BooleanField(default=False)
    retired_at = models.DateTimeField(null=True, blank=True)

    # endregion

    # region Education

    if TYPE_CHECKING:
        educational_institutions: Manager[EducationalInstitution]

    education_level = models.IntegerField(
        choices=EducationLevels.choices,
        default=None,
        null=True,
        blank=True,
    )

    academic_degree = models.IntegerField(
        choices=AcademicDegrees.choices,
        default=None,
        null=True,
        blank=True,
    )

    # endregion

    # region Contacts

    if TYPE_CHECKING:
        phone_numbers: Manager[PhoneNumber]
        addresses: Manager[Address]
        emails: Manager[Email]

    # endregion

    # region Other

    if TYPE_CHECKING:
        comments: Manager[Comment]
        rewards: Manager[Reward]
        relatives: Manager[Relative]

    # endregion
