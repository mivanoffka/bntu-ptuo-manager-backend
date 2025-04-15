from django.urls import path
from users.views import (
    RegisterView,
    ProtectedView,
    CustomTokenObtainPairView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("protected/", ProtectedView.as_view(), name="protected"),
]
