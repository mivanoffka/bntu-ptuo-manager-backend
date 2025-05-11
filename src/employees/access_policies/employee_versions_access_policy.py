from rest_access_policy.access_policy import AccessPolicy
from users.models import UserRoleModel


class EmployeeVersionsAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": [
                "retrieve",
            ],
            "principal": "authenticated",
            "effect": "allow",
        },
        {
            "action": ["destroy", "restore"],
            "principal": "authenticated",
            "effect": "allow",
            "condition": "is_manager",
        },
    ]

    def is_manager(self, request, view, action):
        print("!")
        roles = [UserRoleModel.MANAGER, UserRoleModel.ADMIN]
        return request.user.role in roles

    def is_admin(self, request, view, action):
        return request.user.role == UserRoleModel.ADMIN
