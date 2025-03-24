from django.urls import path
from .views import EmployeeView, SpreadsheetView, GenerateView

urlpatterns = [
    path("employee/", EmployeeView.as_view(), name="employee"),
    path("spreadsheet/", SpreadsheetView.as_view(), name="spreadsheet"),
    path("generate/", GenerateView.as_view(), name="generate"),
]
