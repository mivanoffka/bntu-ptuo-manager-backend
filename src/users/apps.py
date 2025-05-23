from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db import connections, OperationalError, DEFAULT_DB_ALIAS
from django.db.migrations.executor import MigrationExecutor


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
