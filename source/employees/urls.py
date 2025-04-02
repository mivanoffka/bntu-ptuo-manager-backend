from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EmployeeView, SpreadsheetView, GenerateView, EnumerationsView

employees_router = DefaultRouter()
employees_router.register("", EmployeeView, basename="")

urlpatterns = [
    path("", include(employees_router.urls)),
    path("spreadsheet/", SpreadsheetView.as_view(), name="spreadsheet"),
    path("generate/", GenerateView.as_view(), name="generate"),
    path("enumerations/", EnumerationsView.as_view(), name="enumerations"),
]
