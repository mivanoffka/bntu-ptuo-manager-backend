from rest_access_policy.access_policy import AccessPolicy
from users.models import UserRoleModel


class EmployeesAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": [
                "list",
                "export_excel",
                "retrieve",
                "search_for",
            ],
            "principal": "authenticated",
            "effect": "allow",
        },
        {
            "action": [
                "update",
                "partial_update",
                "create",
            ],
            "principal": "authenticated",
            "effect": "allow",
            "condition": "is_editor",
        },
        {
            "action": ["destroy"],
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

    def is_editor(self, request, view, action):
        roles = [UserRoleModel.EDITOR, UserRoleModel.ADMIN, UserRoleModel.MANAGER]
        return request.user.role in roles

    def is_manager(self, request, view, action):
        roles = [UserRoleModel.MANAGER, UserRoleModel.ADMIN]
        return request.user.role in roles

    def is_admin(self, request, view, action):
        return request.user.role == UserRoleModel.ADMIN
