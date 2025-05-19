from .employee_version_serializer import EmployeeVersionSerializer
from .employee_serializer import EmployeeSerializer
from .employee_version_plain_serializer import EmployeeVersionPlainSerializer

from .bntu import BntuPositionSerializer
from .other import (
    CommentSerializer,
    RelativeSerializer,
    RewardSerializer,
)
from .contacts import (
    PhoneNumberSerializer,
    EmailSerializer,
    AddressSerializer,
)
from .education import (
    EducationalInstitutionSerializer,
)

from .utils import GenerateEmployeesSerializer
