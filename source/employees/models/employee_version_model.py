from __future__ import annotations

from typing import TYPE_CHECKING
from django.db import models

from .employee_model import EmployeeModel

from .gender_model import GenderModel
from .level_model import EducationLevelModel
from .academic_degree_model import AcademicDegreeModel


if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager
    from .common import NameModel
    from .bntu import BntuPositionModel
    from .contacts import PhoneNumberModel, AddressModel, EmailModel
    from .trade_union import (
        TradeUnionDepartmentRecordModel,
        WorkingGroupRecordModel,
        TradeUnionPositionModel,
    )
    from .other import RelativeModel, RewardModel, CommentModel
    from .education import EducationalInstitutionModel


class EmployeeVersionModel(models.Model):
    class Meta:
        db_table = "employee_versions"

    # region Common

    id = models.AutoField(primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True)

    employee = models.ForeignKey(
        EmployeeModel, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    if TYPE_CHECKING:
        names: RelatedManager[NameModel]

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
        bntu_positions: RelatedManager[BntuPositionModel]

    # endregion

    # region Trade union

    if TYPE_CHECKING:
        trade_union_department_records: RelatedManager[TradeUnionDepartmentRecordModel]
        working_groups_record: RelatedManager[WorkingGroupRecordModel]
        trade_union_positions: RelatedManager[TradeUnionPositionModel]

    joined_at = models.DateTimeField(null=True, blank=True)
    recorded_at = models.DateTimeField(null=True, blank=True)
    is_archived = models.BooleanField(default=False)
    archived_at = models.DateTimeField(null=True, blank=True)
    is_retired = models.BooleanField(default=False)
    retired_at = models.DateTimeField(null=True, blank=True)

    # endregion

    # region Education

    if TYPE_CHECKING:
        educational_institutions: RelatedManager[EducationalInstitutionModel]

    education_level = models.ForeignKey(
        EducationLevelModel,
        on_delete=models.CASCADE,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )
    academic_degree = models.ForeignKey(
        AcademicDegreeModel,
        on_delete=models.CASCADE,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )

    # endregion

    # region Contacts

    if TYPE_CHECKING:
        phone_numbers: RelatedManager[PhoneNumberModel]
        addresses: RelatedManager[AddressModel]
        emails: RelatedManager[EmailModel]

    # endregion

    # region Other

    if TYPE_CHECKING:
        comments: RelatedManager[CommentModel]
        rewards: RelatedManager[RewardModel]
        relatives: RelatedManager[RelativeModel]

    # endregion
