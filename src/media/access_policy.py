from rest_access_policy.access_policy import AccessPolicy


class EmployeesAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve", "create"],
            "principal": "authenticated",
            "effect": "allow",
        },
        {
            "action": ["update", "partial_update", "destroy"],
            "principal": "authenticated",
            "effect": "deny",
        },
    ]
