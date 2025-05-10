from rest_access_policy.access_policy import AccessPolicy
from users.models import UserRoleModel


class EmployeesAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": [
                "list",
                "export_excel",
                "create",
                "update",
                "partial_update",
                "retrieve",
                "get_version_by_timestamp",
            ],
            "principal": "authenticated",
            "effect": "allow",
        },
        {
            "action": ["restore", "delete_version_by_timestamp", "destroy"],
            "principal": "authenticated",
            "effect": "allow",
            "condition": "is_manager",
        },
        {
            "action": ["generate", "reset"],
            "principal": "authenticated",
            "effect": "allow",
            "condition": "is_admin",
        },
    ]

    def is_manager(self, request, view, action):
        roles = [UserRoleModel.MANAGER, UserRoleModel.ADMIN]
        return request.user.role in roles

    def is_admin(self, request, view, action):
        return request.user.role == UserRoleModel.ADMIN
