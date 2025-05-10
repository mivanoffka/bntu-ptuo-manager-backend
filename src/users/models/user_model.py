from django.contrib.auth.models import AbstractUser
from django.db import models

from .user_role_model import UserRoleModel


class UserModel(AbstractUser):
    role = models.CharField(
        max_length=10, choices=UserRoleModel.choices, default=UserRoleModel.VIEWER
    )

    is_verified = models.BooleanField(default=False)

    def is_admin(self):
        return self.role == UserRoleModel.ADMIN

    def is_manager(self):
        return self.role == UserRoleModel.MANAGER

    def is_editor(self):
        return self.role == UserRoleModel.EDITOR
