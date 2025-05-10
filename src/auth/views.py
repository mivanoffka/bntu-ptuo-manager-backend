from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.utils import no_body

from users.serializers import UserSerializer


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

    @swagger_auto_schema(
        method="post",
        request_body=SignUpSerializer,
        responses={201: UserSerializer},
    )
    @action(detail=False, methods=["post"], url_path="sign-up")
    def sign_up(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            response_serializer = UserSerializer(serializer.instance)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
