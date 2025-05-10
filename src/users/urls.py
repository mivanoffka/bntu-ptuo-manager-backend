from django.urls import path
from users.views import (
    SignUpView,
    ProtectedView,
    SignInView,
)

urlpatterns = [
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    path("sign-in/", SignInView.as_view(), name="sign-in"),
    path("protected/", ProtectedView.as_view(), name="protected"),
]
