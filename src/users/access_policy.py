from rest_access_policy.access_policy import AccessPolicy
from .models import UserRoleModel


class UsersAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["*"],
            "principal": "authenticated",
            "effect": "allow",
            "condition": "is_admin",
        },
    ]

    def is_admin(self, request, view, role):
        return request.user.role == UserRoleModel.ADMIN
