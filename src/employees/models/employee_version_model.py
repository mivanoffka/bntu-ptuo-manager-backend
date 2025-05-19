from __future__ import annotations

from typing import TYPE_CHECKING
from django.db import models


from .employee_model import EmployeeModel

from references.models import (
    GenderModel,
    WorkingGroupModel,
    AcademicDegreeModel,
    EducationLevelModel,
)

from media.models import ImageModel

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager
    from .bntu import BntuPositionModel
    from .contacts import PhoneNumberModel, AddressModel, EmailModel
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

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)

    gender = models.ForeignKey(
        GenderModel,
        on_delete=models.SET_NULL,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )

    birthdate = models.DateTimeField(null=True, blank=True)
    birthplace = models.CharField(max_length=256, null=True, blank=True)

    image = models.ForeignKey(
        ImageModel,
        on_delete=models.SET_NULL,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )

    # endregion

    # region BNTU

    if TYPE_CHECKING:
        bntu_positions: RelatedManager[BntuPositionModel]

    # endregion

    # region Trade union

    trade_union_membership_number = models.CharField(
        max_length=255, null=True, blank=True
    )

    working_group = models.ForeignKey(
        WorkingGroupModel,
        on_delete=models.SET_NULL,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )
    working_group_authentic_label = models.CharField(max_length=255, null=True)

    trade_union_department_path = models.CharField(max_length=255, null=True)
    trade_union_department_authentic_label = models.CharField(max_length=255, null=True)

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
        on_delete=models.SET_NULL,
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
