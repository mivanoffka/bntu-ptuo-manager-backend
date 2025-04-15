from .employee_version_serializer import EmployeeVersionSerializer
from .employee_serializer import EmployeeSerializer

from .bntu import BntuPositionSerializer
from .trade_union import (
    TradeUnionPositionSerializer,
)
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

from .generic import EnumeratedSerializer, TreeNodeSerializer

from .tree_serializer import (
    BntuDepartmentOptionSerializer,
    TreeSerializer,
    TradeUnionDepartmentOptionSerializer,
)
