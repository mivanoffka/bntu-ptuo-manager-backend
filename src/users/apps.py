from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError

from .models.user_role_model import UserRoleModel


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self):
        from django.db import connections

        try:
            db_conn = connections["default"]
            db_conn.ensure_connection()
        except OperationalError:
            return

        UserModel = get_user_model()
        if not UserModel.objects.filter(is_superuser=True).exists():
            print("Creating default superuser...")
            try:
                UserModel.objects.create_superuser(
                    username="admin",
                    email="admin@example.com",
                    password="admin",
                    is_verified=True,
                    role=UserRoleModel.ADMIN,
                )
                print("Superuser created.")
            except Exception as e:
                print("Error creating superuser:", e)
