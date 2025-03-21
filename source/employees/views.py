from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status

from .models import Name

from .serializers.employee import EmployeeSerializer
from .models import Employee
from users.serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class Spreadsheet(APIView):
    def get(self, request): ...


# Create your views here.
class EmployeeView(APIView):
    def post(self, request): ...

    def get(self, request):
        employee = Employee.objects.create(
            birthdate=None,
            gender=None,
            is_archived=False,
            is_retired=False,
        )

        name = Name.objects.create(
            employee=employee,
            first_name="John",
            last_name="Doe",
            middle_name="A",
        )

        return Response({"employee": EmployeeSerializer(employee).data})
