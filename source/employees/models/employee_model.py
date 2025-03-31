from __future__ import annotations

from typing import TYPE_CHECKING
from django.db import models

from .gender_model import GenderModel
from .level_model import EducationLevelModel
from .academic_degree_model import AcademicDegree


if TYPE_CHECKING:
    from django.db.models import Manager
    from .common import NameModel
    from .bntu import BntuPositionModel
    from .contacts import PhoneNumberModel, AddressModel, EmailModel
    from .trade_union import (
        TradeUnionDepartmentModel,
        WorkingGroupModel,
        TradeUnionPositionModel,
    )
    from .other import RelativeModel, RewardModel, CommentModel
    from .education import EducationalInstitutionModel


class EmployeeModel(models.Model):
    class Meta:
        db_table = "employees"

    # region Common

    if TYPE_CHECKING:
        names: Manager[NameModel]

    id = models.AutoField(primary_key=True)

    gender = models.ForeignKey(
        GenderModel,
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
        bntu_positions: Manager[BntuPositionModel]

    # endregion

    # region Trade union

    if TYPE_CHECKING:
        trade_union_departments: Manager[TradeUnionDepartmentModel]
        working_groups: Manager[WorkingGroupModel]
        trade_union_positions: Manager[TradeUnionPositionModel]

    joined_at = models.DateTimeField(null=True, blank=True)
    recorded_at = models.DateTimeField(null=True, blank=True)
    is_archived = models.BooleanField(default=False)
    archived_at = models.DateTimeField(null=True, blank=True)
    is_retired = models.BooleanField(default=False)
    retired_at = models.DateTimeField(null=True, blank=True)

    # endregion

    # region Education

    if TYPE_CHECKING:
        educational_institutions: Manager[EducationalInstitutionModel]

    education_level = models.ForeignKey(
        EducationLevelModel,
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
        phone_numbers: Manager[PhoneNumberModel]
        addresses: Manager[AddressModel]
        emails: Manager[EmailModel]

    # endregion

    # region Other

    if TYPE_CHECKING:
        comments: Manager[CommentModel]
        rewards: Manager[RewardModel]
        relatives: Manager[RelativeModel]

    # endregion
