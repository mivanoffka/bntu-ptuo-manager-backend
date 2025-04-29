from django.urls import path
from .views import TreesAPIView

urlpatterns = [
    path("", TreesAPIView.as_view(), name=""),
]
