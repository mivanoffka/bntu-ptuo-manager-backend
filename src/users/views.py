import re
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .access_policy import UsersAccessPolicy
from .models.user_role_model import UserRoleModel
from users.models import UserModel
from users.serializers import UserSerializer
from rest_framework.decorators import action
from drf_yasg.utils import no_body, swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination


class UsersPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "limit"


@permission_classes([UsersAccessPolicy])
class UsersViewSet(viewsets.ModelViewSet):
    pagination_class = UsersPagination

    queryset = UserModel.objects.all().order_by("date_joined")
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["date_joined", "is_verified", "role"]

    @swagger_auto_schema(
        method="patch",
        responses={
            200: openapi.Response("User verified successfully", UserSerializer),
            409: openapi.Response("User already verified"),
            404: openapi.Response("User not found"),
        },
        request_body=no_body,
    )
    @action(detail=True, methods=["patch"], url_path="verify", url_name="verify")
    def verify(self, request, pk=None):
        try:
            user = self.get_object()

            if user.is_verified:
                return Response(
                    {"detail": "User already verified"},
                    status=status.HTTP_409_CONFLICT,
                )

            user.is_verified = True
            user.save()
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            return Response(
                {"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

    @swagger_auto_schema(
        method="delete",
        responses={
            204: openapi.Response("User declined successfully"),
            409: openapi.Response("Verified users cannot be declined"),
            404: openapi.Response("User not found"),
        },
        request_body=no_body,
    )
    @action(detail=True, methods=["delete"], url_path="decline", url_name="decline")
    def decline(self, request, pk=None):
        try:
            user = self.get_object()

            if user.is_verified:
                return Response(
                    {"detail": "Verified users cannot be declined"},
                    status=status.HTTP_409_CONFLICT,
                )

            user.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except UserModel.DoesNotExist:
            return Response(
                {"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

    @swagger_auto_schema(
        method="patch",
        responses={
            200: openapi.Response("User role updated successfully", UserSerializer),
            404: openapi.Response("User not found"),
            400: openapi.Response("Invalid role"),
            409: openapi.Response("You cannot change your own role"),
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={"role": openapi.Schema(type=openapi.TYPE_STRING)},
            required=["role"],
        ),
    )
    @action(detail=True, methods=["patch"], url_path="role", url_name="role")
    def update_role(self, request, pk=None):
        try:
            user = self.get_object()

            if user == request.user:
                return Response(
                    {"detail": "You cannot change your own role"},
                    status=status.HTTP_409_CONFLICT,
                )

            role = request.data["role"]

            if role not in (choice[0] for choice in UserRoleModel.choices):
                return Response(
                    {"detail": "Invalid role"}, status=status.HTTP_400_BAD_REQUEST
                )

            user.role = role
            user.save()
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            return Response(
                {"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, *args, **kwargs):
        return Response(
            {"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def partial_update(self, request, *args, **kwargs):
        return Response(
            {"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def create(self, request, *args, **kwargs):
        return Response(
            {"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def delete(self, request, *args, **kwargs):
        return Response(
            {"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    @swagger_auto_schema(
        method="get",
        responses={
            200: openapi.Response(
                "Current user retrieved successfully", UserSerializer
            ),
            401: openapi.Response("Unauthorized"),
        },
    )
    @action(detail=False, methods=["get"], url_path="user", url_name="user")
    def get_current_user(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
