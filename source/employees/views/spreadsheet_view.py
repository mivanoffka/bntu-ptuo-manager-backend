from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status

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
)

from ..serializers import EmployeeSerializer
from users.serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from datetime import datetime, date


class SpreadsheetView(APIView):
    def get(self, request):
        employees = EmployeeModel.objects.all()
        employees_s = [EmployeeSerializer(employee).data for employee in employees]

        return Response({"employees": employees_s})
