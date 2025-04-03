from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import models


from ..models import (
    WorkingGroupModel,
    TradeUnionDepartmentModel,
    TradeUnionPositionModel,
    BntuDepartmentModel,
    BntuPositionModel,
    PhoneNumberTypeModel,
    PhoneNumberModel,
    EmailModel,
    EducationalInstitutionModel,
    EducationLevelModel,
    GenderModel,
    NameModel,
    EmployeeModel,
    AddressModel,
    AcademicDegreeModel,
    WorkingGroupOptionModel,
    TradeUnionDepartmentOptionModel,
    RelativeModel,
    RelativeTypeModel,
    RewardModel,
    CommentModel,
)

from ..serializers import EmployeeSerializer
import random

from faker import Faker


class GenerateView(APIView):
    _faker = Faker()

    def _get_random_object(self, Type: type[models.Model]):
        return random.choice(Type.objects.all())

    def _get_random_count(self):
        return random.randint(1, 2)

    def _get_random_comment(self):
        chance = random.randint(0, 3)
        if chance == 0:
            return self._faker.text(50)
        else:
            return None

    def _add_random_names(self, employee: EmployeeModel):
        for i in range(self._get_random_count()):
            NameModel.objects.create(
                employee=employee,
                first_name=self._faker.first_name(),
                last_name=self._faker.first_name(),
                middle_name=self._faker.first_name(),
            )

    def _add_random_emails(self, employee: EmployeeModel):
        for i in range(self._get_random_count()):
            EmailModel.objects.create(
                employee=employee,
                value=self._faker.email(),
                comment=self._get_random_comment(),
            )

    def _add_random_addresses(self, employee: EmployeeModel):
        for i in range(self._get_random_count()):
            AddressModel.objects.create(
                employee=employee,
                value=self._faker.address(),
                comment=self._get_random_comment(),
            )

    def _add_random_phone_numbers(self, employee: EmployeeModel):
        for i in range(self._get_random_count()):
            PhoneNumberModel.objects.create(
                employee=employee,
                value=self._faker.phone_number(),
                phone_number_type=self._get_random_object(PhoneNumberTypeModel),
                comment=self._get_random_comment(),
            )

    def _add_random_education_institutions(self, employee: EmployeeModel):
        for i in range(self._get_random_count()):
            EducationalInstitutionModel.objects.create(
                employee=employee,
                label=self._faker.company(),
                graduated_at=self._faker.date(),
                comment=self._get_random_comment(),
            )

    def _add_random_bntu_positions(self, employee: EmployeeModel):
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

            BntuPositionModel.objects.create(
                employee=employee,
                label=self._faker.text(30),
                hired_at=self._faker.date(),
                discharged_at=discharged_at,
                is_discharged_voluntarily=is_discharged_voluntarily,
                dischargement_comment=dischargement_comment,
                department=self._get_random_object(BntuDepartmentModel),
            )

    def _add_random_trade_union_info(self, employee: EmployeeModel):
        self._add_random_working_groups(employee)
        self._add_random_trade_union_departments(employee)
        self._add_random_trade_union_positions(employee)

    def _add_random_working_groups(self, employee: EmployeeModel):
        for i in range(self._get_random_count()):
            WorkingGroupModel.objects.create(
                employee=employee,
                working_group_option=self._get_random_object(WorkingGroupOptionModel),
            )

    def _add_random_trade_union_departments(self, employee: EmployeeModel):
        for i in range(self._get_random_count()):
            TradeUnionDepartmentModel.objects.create(
                employee=employee,
                trade_union_department_option=self._get_random_object(
                    TradeUnionDepartmentOptionModel
                ),
            )

    def _add_random_trade_union_positions(self, employee: EmployeeModel):
        for i in range(self._get_random_count()):
            TradeUnionPositionModel.objects.create(
                employee=employee,
                label=self._faker.text(30),
                occurred_at=self._faker.date(),
                comment=self._get_random_comment(),
            )

    def _add_random_relatives(self, employee: EmployeeModel):
        for i in range(self._get_random_count()):
            RelativeModel.objects.create(
                employee=employee,
                birthdate=self._faker.date(),
                relative_type=self._get_random_object(RelativeTypeModel),
                full_name=self._faker.name(),
                comment=self._get_random_comment(),
            )

    def _add_random_rewards(self, employee: EmployeeModel):
        for i in range(self._get_random_count()):
            RewardModel.objects.create(
                employee=employee,
                label=self._faker.text(30),
                granted_at=self._faker.date(),
                comment=self._get_random_comment(),
            )

    def _add_random_comments(self, employee: EmployeeModel):
        for i in range(self._get_random_count()):
            CommentModel.objects.create(
                employee=employee,
                value=self._faker.text(100),
            )

    def post(self, request):
        is_archived = random.randint(0, 4)
        archived_at = self._faker.date() if not is_archived else None
        is_archived = not bool(is_archived)

        is_retired = random.randint(0, 4)
        retired_at = self._faker.date() if not is_retired else None
        is_retired = not bool(is_retired)

        employee = EmployeeModel.objects.create(
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

        self._add_random_names(employee)
        self._add_random_emails(employee)
        self._add_random_addresses(employee)
        self._add_random_phone_numbers(employee)
        self._add_random_education_institutions(employee)
        self._add_random_bntu_positions(employee)
        self._add_random_trade_union_info(employee)
        self._add_random_relatives(employee)
        self._add_random_rewards(employee)
        self._add_random_comments(employee)

        return Response({"employee": EmployeeSerializer(employee).data})
