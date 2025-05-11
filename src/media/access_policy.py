from rest_access_policy.access_policy import AccessPolicy

from ..users.models import UserRoleModel


class EmployeesAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": [
                "list",
                "retrieve",
            ],
            "principal": "authenticated",
            "effect": "allow",
        },
        {
            "action": ["create"],
            "principal": "authenticated",
            "effect": "allow",
            "condition": "is_editor",
        },
        {
            "action": ["update", "partial_update", "destroy"],
            "principal": "authenticated",
            "effect": "deny",
        },
    ]

    def is_editor(self, request, view, action):
        roles = [UserRoleModel.EDITOR, UserRoleModel.ADMIN, UserRoleModel.MANAGER]
        return request.user.role in roles
