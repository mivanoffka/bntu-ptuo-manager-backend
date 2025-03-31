from __future__ import annotations

from typing import TYPE_CHECKING
from django.db import models

from .gender import Gender
from .level import EducationLevel
from .degrees import AcademicDegree


if TYPE_CHECKING:
    from django.db.models import Manager
    from .common import Name
    from .bntu import BntuPosition
    from .contacts import PhoneNumber, Address, Email
    from .trade_union import TradeUnionDepartment, WorkingGroup, TradeUnionPosition
    from .other import Relative, Reward, Comment
    from .education import EducationalInstitution


class Employee(models.Model):
    class Meta:
        db_table = "employees"

    # region Common

    if TYPE_CHECKING:
        names: Manager[Name]

    id = models.AutoField(primary_key=True)

    gender = models.ForeignKey(
        Gender,
        on_delete=models.CASCADE,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )

    birthdate = models.DateTimeField(null=True, blank=True)
    birthplace = models.CharField(max_length=256, null=True, blank=True)

    # endregion

    # region BNTU

    if TYPE_CHECKING:
        bntu_positions: Manager[BntuPosition]

    # endregion

    # region Trade union

    if TYPE_CHECKING:
        trade_union_departments: Manager[TradeUnionDepartment]
        working_groups: Manager[WorkingGroup]
        trade_union_positions: Manager[TradeUnionPosition]

    joined_at = models.DateTimeField(null=True, blank=True)
    recorded_at = models.DateTimeField(null=True, blank=True)
    is_archived = models.BooleanField(default=False)
    archived_at = models.DateTimeField(null=True, blank=True)
    is_retired = models.BooleanField(default=False)
    retired_at = models.DateTimeField(null=True, blank=True)

    # endregion

    # region Education

    if TYPE_CHECKING:
        educational_institutions: Manager[EducationalInstitution]

    education_level = models.ForeignKey(
        EducationLevel,
        on_delete=models.CASCADE,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )
    academic_degree = models.ForeignKey(
        AcademicDegree,
        on_delete=models.CASCADE,
        related_name=Meta.db_table,
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
