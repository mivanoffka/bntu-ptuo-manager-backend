from django.db import models


class UserRoleModel(models.TextChoices):
    ADMIN = "admin", "Admin"
    MANAGER = "manager", "Manager"
    EDITOR = "editor", "Editor"
    VIEWER = "viewer", "Viewer"
