from typing import TypeVar
from rest_framework.views import APIView
from rest_framework.response import Response


from ..models import (
    WorkingGroup,
    TradeUnionDepartment,
    TradeUnionPositionName,
    TradeUnionPosition,
    BntuDepartment,
    BntuPositionName,
    BntuPosition,
    PhoneNumberType,
    PhoneNumber,
    Email,
    EducationalInstitution,
    EducationLevel,
    Gender,
    Name,
    Employee,
    Address,
    AcademicDegree,
)

from ..serializers import EmployeeSerializer
import random

from faker import Faker
from datetime import datetime
from django.db.models import Manager, Model


class GenerateView(APIView):
    _faker = Faker()

    def _get_random_object(self, Type: type[Model]):
        return random.choice(Type.objects.all())

    def _get_random_count(self):
        return random.randint(1, 2)

    def _get_random_comment(self):
        return self._faker.text(50) if random.randint(-2, 1) > 0 else None

    def _add_random_names(self, employee: Employee):
        for i in range(self._get_random_count()):
            Name.objects.create(
                employee=employee,
                first_name=self._faker.first_name(),
                last_name=self._faker.first_name(),
                middle_name=self._faker.first_name(),
            )

    def _add_random_emails(self, employee: Employee):
        for i in range(self._get_random_count()):
            Email.objects.create(
                employee=employee,
                value=self._faker.email(),
                comment=self._get_random_comment(),
            )

    def _add_random_addresses(self, employee: Employee):
        for i in range(self._get_random_count()):
            Address.objects.create(
                employee=employee,
                value=self._faker.address(),
                comment=self._get_random_comment(),
            )

    def _add_random_phone_numbers(self, employee: Employee):
        for i in range(self._get_random_count()):
            PhoneNumber.objects.create(
                employee=employee,
                value=self._faker.phone_number(),
                phone_number_type=self._get_random_object(PhoneNumberType),
                comment=self._get_random_comment(),
            )

    def _add_random_education_institutions(self, employee: Employee):
        for i in range(self._get_random_count()):
            is_old = random.randint(0, 6)
            institution: EducationalInstitution
            if is_old:
                institution = EducationalInstitution.objects.create(
                    label=self._faker.company()
                )
            else:
                institution = self._get_random_object(EducationalInstitution)  # type: ignore

            institution.employees.add(employee)
            employee.educational_institutions.add(institution)

    def _add_random_bntu_positions(self, employee: Employee):
        for i in range(self._get_random_count()):
            is_discharged_voluntarily = None
            dischargement_comment = None
            is_not_discharged = random.randint(0, 5)
            discharged_at = None

            if not is_not_discharged:
                discharged_at = self._faker.date()
                is_discharged_voluntarily = random.randint(0, 5)
                if not is_discharged_voluntarily:
                    dischargement_comment = self._faker.text(35)

            BntuPosition.objects.create(
                employee=employee,
                name=self._get_random_object(BntuPositionName),
                hired_at=self._faker.date(),
                discharged_at=discharged_at,
                is_discharged_voluntarily=is_discharged_voluntarily,
                dischargement_comment=dischargement_comment,
                department=self._get_random_object(BntuDepartment),
            )

    def _add_random_trade_union_positions(self, employee: Employee):
        for i in range(self._get_random_count()):

            TradeUnionPosition.objects.create(
                employee=employee,
                department=self._get_random_object(TradeUnionDepartment),
                name=self._get_random_object(TradeUnionPositionName),
                working_group=self._get_random_object(WorkingGroup),
                joined_at=self._faker.date(),
                left_at=self._faker.date() if not self._get_random_count() else None,
            )

    def post(self, request):
        employee = Employee.objects.create(
            birthdate=self._faker.date(),
            birthplace=self._faker.city(),
            joined_at=self._faker.date(),
            gender=self._get_random_object(Gender),
            education_level=self._get_random_object(EducationLevel),
            academic_degree=self._get_random_object(AcademicDegree),
        )

        self._add_random_names(employee)
        self._add_random_emails(employee)
        self._add_random_addresses(employee)
        self._add_random_phone_numbers(employee)
        self._add_random_education_institutions(employee)
        self._add_random_bntu_positions(employee)
        self._add_random_trade_union_positions(employee)

        return Response({"employee": EmployeeSerializer(employee).data})
