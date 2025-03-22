from django.urls import path
from .views import EmployeeView, SpreadsheetView

urlpatterns = [
    path("employee/", EmployeeView.as_view(), name="employee"),
    path("spreadsheet/", SpreadsheetView.as_view(), name="spreadsheet"),
]
