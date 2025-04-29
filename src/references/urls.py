from django.urls import path
from .views import ReferencesAPIView

urlpatterns = [
    path("", ReferencesAPIView.as_view(), name=""),
]
