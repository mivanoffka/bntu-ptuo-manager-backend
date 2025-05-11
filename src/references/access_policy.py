from rest_access_policy.access_policy import AccessPolicy
from users.models import UserRoleModel


class ReferencesAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["partial_update", "update", "destroy", "create"],
            "principal": "authenticated",
            "effect": "allow",
            "condition": "is_manager",
        },
        {
            "action": ["list", "retrieve"],
            "principal": "authenticated",
            "effect": "allow",
        },
    ]

    def is_manager(self, request, view, role):
        roles = [UserRoleModel.MANAGER, UserRoleModel.ADMIN]

        return request.user.role in roles
