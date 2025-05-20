from rest_access_policy.access_policy import AccessPolicy
from .models import UserRoleModel


class UsersAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["get_current_user"],
            "principal": "authenticated",
            "effect": "allow",
        },
        {
            "action": ["*"],
            "principal": "authenticated",
            "effect": "allow",
            "condition": "is_admin",
        },
    ]

    def is_admin(self, request, view, role):
        return request.user.role == UserRoleModel.ADMIN
