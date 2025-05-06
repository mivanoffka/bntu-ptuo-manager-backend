from typing import Type, TypeVar

from django.db import models

from references.models import (
    PhoneNumberTypeModel,
    RelativeTypeModel,
    GenderModel,
    AcademicDegreeModel,
    EducationLevelModel,
    WorkingGroupModel,
)

from trees.models import BntuDepartmentModel, TradeUnionDepartmentModel

from ..models import (
    EmployeeModel,
    TradeUnionPositionModel,
    BntuPositionModel,
    PhoneNumberModel,
    EmailModel,
    EducationalInstitutionModel,
    EmployeeVersionModel,
    AddressModel,
    RelativeModel,
    RewardModel,
    CommentModel,
)

import random

from faker import Faker


class EmployeeGenerator:
    _faker = Faker("ru_RU")

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

            bntu_department: BntuDepartmentModel = self._get_random_object(
                BntuDepartmentModel
            )

            bntu_department_authentic_label = bntu_department.label

            BntuPositionModel.objects.create(
                employee_version=employee_version,
                label=self._faker.job(),
                hired_at=self._faker.date(),
                discharged_at=discharged_at,
                is_discharged_voluntarily=is_discharged_voluntarily,
                dischargement_comment=dischargement_comment,
                bntu_department_path=bntu_department.path,
                bntu_department_authentic_label=bntu_department_authentic_label,
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

    def generate(self, count: int = 1):
        employees = []

        for i in range(count):
            employees.append(self._generate_one())

        return employees

    def _generate_one(self) -> EmployeeModel:
        employee = EmployeeModel.objects.create()

        is_archived = random.randint(0, 4)
        archived_at = self._faker.date() if not is_archived else None
        is_archived = not bool(is_archived)

        is_retired = random.randint(0, 4)
        retired_at = self._faker.date() if not is_retired else None
        is_retired = not bool(is_retired)

        gender = self._get_random_object(GenderModel)

        employee_version = EmployeeVersionModel.objects.create(
            employee=employee,
            first_name=(
                self._faker.first_name_male()
                if gender.id == 1
                else self._faker.first_name_female()
            ),
            last_name=(
                self._faker.last_name_male()
                if gender.id == 1
                else self._faker.last_name_female()
            ),
            middle_name=(
                self._faker.middle_name_male()
                if gender.id == 1
                else self._faker.middle_name_female()
            ),
            birthdate=self._faker.date(),
            birthplace=self._faker.city(),
            joined_at=self._faker.date(),
            recorded_at=self._faker.date(),
            gender=gender,
            working_group=self._get_random_object(WorkingGroupModel),
            trade_union_department_path=self._get_random_object(
                TradeUnionDepartmentModel
            ).path,
            education_level=self._get_random_object(EducationLevelModel),
            academic_degree=self._get_random_object(AcademicDegreeModel),
            is_archived=is_archived,
            archived_at=archived_at,
            is_retired=is_retired,
            retired_at=retired_at,
        )

        self._add_random_emails(employee_version)
        self._add_random_addresses(employee_version)
        self._add_random_phone_numbers(employee_version)
        self._add_random_education_institutions(employee_version)
        self._add_random_bntu_positions(employee_version)
        self._add_random_trade_union_positions(employee_version)
        self._add_random_relatives(employee_version)
        self._add_random_rewards(employee_version)
        self._add_random_comments(employee_version)

        employee.employee_versions.add(employee_version)

        return employee
