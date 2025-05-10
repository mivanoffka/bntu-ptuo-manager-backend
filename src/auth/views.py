from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serializers import (
    SignInRequestSerializer,
    SignInResponseSerializer,
    SignUpSerializer,
)


class AuthViewSet(ViewSet):
    @swagger_auto_schema(
        method="post",
        request_body=SignInRequestSerializer,
        responses={200: SignInResponseSerializer},
    )
    @action(detail=False, methods=["post"], url_path="sign-in")
    def sign_in(self, request):
        serializer = SignInRequestSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data

            response_serializer = SignInResponseSerializer(user)

            return Response(response_serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], url_path="sign-up")
    def sign_up(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
