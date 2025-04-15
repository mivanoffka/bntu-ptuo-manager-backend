from typing import Type, TypeVar

from django.db import models

from ..models import (
    EmployeeModel,
    WorkingGroupRecordModel,
    TradeUnionDepartmentRecordModel,
    TradeUnionPositionModel,
    BntuDepartmentOptionModel,
    BntuPositionModel,
    PhoneNumberTypeModel,
    PhoneNumberModel,
    EmailModel,
    EducationalInstitutionModel,
    EducationLevelModel,
    GenderModel,
    NameModel,
    EmployeeVersionModel,
    AddressModel,
    AcademicDegreeModel,
    WorkingGroupOptionModel,
    TradeUnionDepartmentOptionModel,
    RelativeModel,
    RelativeTypeModel,
    RewardModel,
    CommentModel,
)

import random

from faker import Faker


class EmployeeGenerator:
    _faker = Faker()

    T = TypeVar("T", bound=models.Model)

    def _get_random_object(self, model_class: Type[T]) -> T:
        return random.choice(model_class.objects.all())

    def _get_random_count(self):
        return random.randint(1, 2)

    def _get_random_comment(self):
        chance = random.randint(0, 3)
        if chance == 0:
            return self._faker.text(50)
        else:
            return None

    def _add_random_names(self, employee_version: EmployeeVersionModel):
        for i in range(self._get_random_count()):
            NameModel.objects.create(
                employee_version=employee_version,
                first_name=self._faker.first_name(),
                last_name=self._faker.first_name(),
                middle_name=self._faker.first_name(),
            )

    def _add_random_emails(self, employee_version: EmployeeVersionModel):
        for i in range(self._get_random_count()):
            EmailModel.objects.create(
                employee_version=employee_version,
                value=self._faker.email(),
                comment=self._get_random_comment(),
            )

    def _add_random_addresses(self, employee_version: EmployeeVersionModel):
        for i in range(self._get_random_count()):
            AddressModel.objects.create(
                employee_version=employee_version,
                value=self._faker.address(),
                comment=self._get_random_comment(),
            )

    def _add_random_phone_numbers(self, employee_version: EmployeeVersionModel):
        for i in range(self._get_random_count()):
            PhoneNumberModel.objects.create(
                employee_version=employee_version,
                value=self._faker.phone_number(),
                phone_number_type=self._get_random_object(PhoneNumberTypeModel),
                comment=self._get_random_comment(),
            )

    def _add_random_education_institutions(
        self, employee_version: EmployeeVersionModel
    ):
        for i in range(self._get_random_count()):
            EducationalInstitutionModel.objects.create(
                employee_version=employee_version,
                label=self._faker.company(),
                graduated_at=self._faker.date(),
                comment=self._get_random_comment(),
            )

    def _add_random_bntu_positions(self, employee_version: EmployeeVersionModel):
        for i in range(self._get_random_count()):
            is_discharged_voluntarily = None
            dischargement_comment = None
            is_not_discharged = random.randint(0, 5)
            discharged_at = None

            if not is_not_discharged:
                discharged_at = self._faker.date()
                is_discharged_voluntarily = bool(random.randint(0, 5))
                if not is_discharged_voluntarily:
                    dischargement_comment = self._faker.text(35)

            bntu_department_option: BntuDepartmentOptionModel = self._get_random_object(
                BntuDepartmentOptionModel
            )

            bntu_department_authentic_label = bntu_department_option.label

            BntuPositionModel.objects.create(
                employee_version=employee_version,
                label=self._faker.text(30),
                hired_at=self._faker.date(),
                discharged_at=discharged_at,
                is_discharged_voluntarily=is_discharged_voluntarily,
                dischargement_comment=dischargement_comment,
                bntu_department_option=bntu_department_option,
                bntu_department_authentic_label=bntu_department_authentic_label,
            )

    def _add_random_trade_union_info(self, employee_version: EmployeeVersionModel):
        self._add_random_working_groups(employee_version)
        self._add_random_trade_union_departments(employee_version)
        self._add_random_trade_union_positions(employee_version)

    def _add_random_working_groups(self, employee_version: EmployeeVersionModel):
        for i in range(self._get_random_count()):
            working_group_option = self._get_random_object(WorkingGroupOptionModel)

            WorkingGroupRecordModel.objects.create(
                employee_version=employee_version,
                working_group_option=working_group_option,
                authentic_label=working_group_option.label,
            )

    def _add_random_trade_union_departments(
        self, employee_version: EmployeeVersionModel
    ):
        for i in range(self._get_random_count()):
            trade_union_department_option = self._get_random_object(
                TradeUnionDepartmentOptionModel
            )

            TradeUnionDepartmentRecordModel.objects.create(
                employee_version=employee_version,
                trade_union_department_option=trade_union_department_option,
                authentic_label=trade_union_department_option.label,
            )

    def _add_random_trade_union_positions(self, employee_version: EmployeeVersionModel):
        for i in range(self._get_random_count()):
            TradeUnionPositionModel.objects.create(
                employee_version=employee_version,
                label=self._faker.text(30),
                occurred_at=self._faker.date(),
                comment=self._get_random_comment(),
            )

    def _add_random_relatives(self, employee_version: EmployeeVersionModel):
        for i in range(self._get_random_count()):
            RelativeModel.objects.create(
                employee_version=employee_version,
                birthdate=self._faker.date(),
                relative_type=self._get_random_object(RelativeTypeModel),
                full_name=self._faker.name(),
                comment=self._get_random_comment(),
            )

    def _add_random_rewards(self, employee_version: EmployeeVersionModel):
        for i in range(self._get_random_count()):
            RewardModel.objects.create(
                employee_version=employee_version,
                label=self._faker.text(30),
                granted_at=self._faker.date(),
                comment=self._get_random_comment(),
            )

    def _add_random_comments(self, employee_version: EmployeeVersionModel):
        for i in range(self._get_random_count()):
            CommentModel.objects.create(
                employee_version=employee_version,
                value=self._faker.text(100),
            )

    def generate(self) -> EmployeeModel:
        employee = EmployeeModel.objects.create()

        is_archived = random.randint(0, 4)
        archived_at = self._faker.date() if not is_archived else None
        is_archived = not bool(is_archived)

        is_retired = random.randint(0, 4)
        retired_at = self._faker.date() if not is_retired else None
        is_retired = not bool(is_retired)

        employee_version = EmployeeVersionModel.objects.create(
            employee=employee,
            birthdate=self._faker.date(),
            birthplace=self._faker.city(),
            joined_at=self._faker.date(),
            recorded_at=self._faker.date(),
            gender=self._get_random_object(GenderModel),
            education_level=self._get_random_object(EducationLevelModel),
            academic_degree=self._get_random_object(AcademicDegreeModel),
            is_archived=is_archived,
            archived_at=archived_at,
            is_retired=is_retired,
            retired_at=retired_at,
        )

        self._add_random_names(employee_version)
        self._add_random_emails(employee_version)
        self._add_random_addresses(employee_version)
        self._add_random_phone_numbers(employee_version)
        self._add_random_education_institutions(employee_version)
        self._add_random_bntu_positions(employee_version)
        self._add_random_trade_union_info(employee_version)
        self._add_random_relatives(employee_version)
        self._add_random_rewards(employee_version)
        self._add_random_comments(employee_version)

        employee.employee_versions.add(employee_version)

        return employee
